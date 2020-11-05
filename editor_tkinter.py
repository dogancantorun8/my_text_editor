import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os


#kullanıcıdan giris almak istersek kullanıyoruz
class GUI:

    def __init__(self, master):
        master.geometry('800x600')
        master.title('Dogan Text Editor')
        master.resizable(width=False,height=False)
        self.master = master

        self.text=tk.Text(master,font='Calibri 12',bg='light blue')
        self.text.place(x=0,y=0,width=800,height=530)

        self.button_ok = tk.Button(master, text='open', command=self.button_open_handler,bg='light green')
        self.button_ok.place(x=30, y=550, width=60, height=30)

        self.button_saveas = tk.Button(master, text='Save As', command=self.button_saveas_handler,bg='purple')
        self.button_saveas.place(x=100, y=550, width=60, height=30)

        self.button_list = tk.Button(master, text='List', command=self.button_list_handler, bg='orange')
        self.button_list.place(x=170, y=550, width=60, height=30)

        self.text.focus()

    def button_open_handler(self):
        path=filedialog.askopenfilename(title='Select file')
        if path!='': #path variable ile dosya yolunu alıyorum
            try:
                with open(path) as f : #dosyamı okuyorum
                    s=f.read()
                    self.text.insert('1.0',s)
            except Exception as e:
                messagebox.showerror(title='Error',message=e)

    def button_saveas_handler(self):
        path = filedialog.asksaveasfilename(title='Select directory and write file extention')
        if path!='': #path variable ile dosya yolunu alıyorum
            try:
                with open(path,'w') as f : #dosyamı yazıyorum
                    s=self.text.get('1.0','end')
                    f.write(s)
            except Exception as e:
                messagebox.showerror(title='Error',message=e)

    def button_list_handler(self):
        path = filedialog.askdirectory(title='Select Directory')  # sectigim directory pathine erişiyorum
        if path != '':
            result2 = os.listdir(path)
            s = '\n'.join(result2)  # listeyi string haline getirdim
            messagebox.showinfo(title='All files in directory',message=s)  # path icindeki tum dosyaları display ediyorum

root = tk.Tk()
gdb = GUI(root)
root.mainloop()