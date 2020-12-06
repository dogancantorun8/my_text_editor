import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
from PIL import Image
from PIL import ImageTk


# binding_not_defterime uyarlama

class GUI:
    def __init__(self, master):
        master.geometry('800x600')
        master.title('DOGAN PYTHON & TEXT EDITOR ')
        master.resizable(width=False, height=False)
        self.master = master

        # self.check_button_var = tk.IntVar()
        self.radio_button_var = tk.StringVar()
        self.radio_button_var.set('Arial 12')

        # menu nesnemi olusturuyorum
        self.menu_bar = tk.Menu(master)

        self.file_popup = tk.Menu(tearoff=0)
        self.menu_bar.add_cascade(label='File', menu=self.file_popup, font='Arial 12', underline=0)

        self.file_popup.add_command(label='Open...', command=self.file_open_handler, font='Arial 10 bold', underline=1,
                                    accelerator='Ctrl+O')
        master.bind('<Control-o>', self.file_open_handler)

        self.file_popup.add_command(label='Save As...', command=self.file_saveas_handler, font='Arial 10 bold',
                                    underline=0, accelerator='Ctrl+S')
        master.bind('<Control-s>', self.file_saveas_handler)

        self.file_popup.add_command(label='Close', command=self.file_close_handler, font='Arial 10', underline=2,
                                    foreground='blue', state=tk.DISABLED)
        # self.file_popup.add_checkbutton(label='Check Button', variable=self.check_button_var,
        #                                 command=self.file_checkbutton_handler)
        self.file_popup.add_separator()

        self.file_popup.add_command(label='Exit', command=self.master.quit, font='Arial 10', underline=1,
                                    accelerator='Ctrl+E')

        self.edit_popup = tk.Menu(tearoff=0)
        self.edit_popup.add_command(label='Cut', underline=0, command=self.edit_cut_handler,
                                    accelerator='Ctrl+X')
        self.edit_popup.add_command(label='Copy', underline=1, command=self.edit_copy_handler, accelerator='Ctrl+C')
        self.edit_popup.add_command(label='Paste', underline=0, command=self.edit_paste_handler, accelerator='Ctrl+V')
        self.edit_popup.add_separator()

        self.edit_font_popup = tk.Menu(tearoff=0)
        self.edit_popup.add_cascade(label='Font', menu=self.edit_font_popup)
        self.edit_font_popup.add_radiobutton(label='Arial 12', command=self.edit_font_handler, value='Arial 12',
                                             variable=self.radio_button_var)
        self.edit_font_popup.add_radiobutton(label='Consolas 12', command=self.edit_font_handler, value='Consolas 12',
                                             variable=self.radio_button_var)
        self.edit_font_popup.add_radiobutton(label='Verdana 12', command=self.edit_font_handler, value='Verdana 12',
                                             variable=self.radio_button_var)

        # edit kısmı
        self.menu_bar.add_cascade(label='Edit', menu=self.edit_popup, underline=0)
        master.config(menu=self.menu_bar)

        self.text = tk.Text(root, font='Consolas 14', bg='light green')
        self.text.place(x=0, y=64, width=800, height=600)

        # toolbar nesnemi olusturuyorum
        self.toolbar = tk.Frame(master)
        self.toolbar.place(x=0, y=0, width=800, height=64)

        img = tk.PhotoImage(file='open.png')
        self.toolbar_button_open = tk.Button(self.toolbar, command=self.file_open_handler, image=img, padx=0, pady=0)
        self.toolbar_button_open.image = img
        self.toolbar_button_open.place(x=0, y=0, width=64, height=64)

        img = tk.PhotoImage(file='save.png')
        self.toolbar_button_saveas = tk.Button(self.toolbar, command=self.file_saveas_handler, image=img, padx=0,
                                               pady=0)
        self.toolbar_button_saveas.image = img
        self.toolbar_button_saveas.place(x=64, y=0, width=64, height=64)

        img = tk.PhotoImage(file='close.png')
        self.toolbar_button_close = tk.Button(self.toolbar, command=self.file_close_handler, image=img, padx=0, pady=0,
                                              state=tk.DISABLED)
        self.toolbar_button_close.image = img
        self.toolbar_button_close.place(x=128, y=0, width=64, height=64)

        img = tk.PhotoImage(file='exit.png')
        self.toolbar_button_exit = tk.Button(self.toolbar, command=self.master.quit, image=img, padx=0, pady=0)
        self.toolbar_button_exit.image = img
        self.toolbar_button_exit.place(x=192, y=0, width=64, height=64)

        img = tk.PhotoImage(file='cut.png')
        self.toolbar_button_cut = tk.Button(self.toolbar, command=self.edit_cut_handler, image=img, padx=0, pady=0)
        self.toolbar_button_cut.image = img
        self.toolbar_button_cut.place(x=300, y=0, width=64, height=64)
        # Ctrl+x tuşuna basıldıgında kes tetikleniyor
        master.bind('<Control-x>', self.edit_cut_handler)

        img = tk.PhotoImage(file='copy.png')
        self.toolbar_button_copy = tk.Button(self.toolbar, command=self.edit_copy_handler, image=img, padx=0, pady=0)
        self.toolbar_button_copy.image = img
        self.toolbar_button_copy.place(x=364, y=0, width=64, height=64)
        # Ctrl+c tuşuna basıldıgında kopyalama tetikleniyor
        master.bind('<Control-c>', self.edit_copy_handler)

        img = tk.PhotoImage(file='paste.png')
        self.toolbar_button_paste = tk.Button(self.toolbar, command=self.edit_paste_handler, image=img, padx=0, pady=0)
        self.toolbar_button_paste.image = img
        self.toolbar_button_paste.place(x=428, y=0, width=64, height=64)
        # Ctrl+V tuşuna basıldıgında yapıstırma tetikleniyor
        master.bind('<Control-v>', self.edit_paste_handler)

        # my logo adding
        self.my_img=ImageTk.PhotoImage(Image.open("kartal.png"))
        self.my_label= tk.Label(image=self.my_img)
        self.my_label.place(x=700, y=0, width=64, height=64)


        # baglam menusu farenin sag tusuna basıldıgında cıkıyor menu nesnesini alıyorum
        self.text_context_menu = tk.Menu(master, tearoff=0)
        self.text_context_menu.add_command(label='Cut', command=self.edit_cut_handler)
        self.text_context_menu.add_command(label='Copy', command=self.edit_copy_handler)
        self.text_context_menu.add_command(label='Paste', command=self.edit_paste_handler)

        # frame icinde sag tusu basıldıgında tetiklenen fonksiyonum
        self.text.bind('<Button-3>', self.text_mouse_right_press_handler)

        self.toolbar_context_menu = tk.Menu(master, tearoff=0)
        self.toolbar_context_menu.add_command(label='Add')
        self.toolbar_context_menu.add_command(label='Remove')
        self.toolbar_context_menu.add_command(label='Adjust')

        # sag tusa basldıgında contex menun cagrılacagını soyleyen handler bu kısım toolbar icinde calısıyor
        self.toolbar.bind('<Button-3>', self.toolbar_mouse_right_press_handler)

    def file_open_handler(self, *args):
        try:
            path = tk.filedialog.askopenfilename(title='Dosya Seçimi',
                                                 filetypes=[('Python Files', '*.py'), ('Text Files', '*.txt')])
            if path != '':
                with open(path) as f:
                    self.text.delete('1.0', 'end')
                    self.text.insert('1.0', f.read())
            self.file_popup.entryconfig(2, state=tk.NORMAL)
            self.file_popup.entryconfig(0, state=tk.DISABLED)
            self.toolbar_button_open.config(state=tk.DISABLED)
            self.toolbar_button_close.config(state=tk.NORMAL)

        except Exception as e:
            tk.messagebox.showerror(title='Error', message=str(e))

    # handler icerisinde *args ile istenilen kadar parametre gonderilebilir
    def file_saveas_handler(self, *args):
        try:
            path = tk.filedialog.asksaveasfilename(title='Dosya Seçimi',
                                                   filetypes=[('Python Files', '*.py'), ('Text Files', '*.txt')])
            if path != '':
                print(path)
                with open(path, 'w') as f:
                    s = self.text.get('1.0', 'end')
                    f.write(s)
        except Exception as e:
            tk.messagebox.showerror(title='Error', message=str(e))

    def file_close_handler(self, *args):
        self.text.delete('1.0', 'end')
        self.file_popup.entryconfig(0, state=tk.NORMAL)
        self.file_popup.entryconfig(2, state=tk.DISABLED)
        self.toolbar_button_open.config(state=tk.NORMAL)
        self.toolbar_button_close.config(state=tk.DISABLED)

    def edit_cut_handler(self, *args):
        print('Cut')

    def edit_copy_handler(self, *args):
        print('Copy')

    def edit_paste_handler(self, *args):
        print('Paste')

    def edit_font_handler(self):
        self.text['font'] = self.radio_button_var.get()

    # def file_checkbutton_handler(self):
    #     print('Checked' if self.check_button_var.get() else 'Unchecked')

    # farenin tuslarına basılınca yapılanlar;
    def text_mouse_right_press_handler(self, event):
        self.text_context_menu.post(event.x_root, event.y_root)
        return 'break'

    def toolbar_mouse_right_press_handler(self, event):
        self.toolbar_context_menu.post(event.x_root, event.y_root)
        return 'break'


root = tk.Tk()
gdb = GUI(root)
root.mainloop()
