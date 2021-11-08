from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from googletrans import Translator



class App:

    def __init__(self, root):
        ttk.Style().configure("TLabel", foreground="white", background="black")
        self.label = Label(root,  text="Введите текст на любом языке", font=("Comic Sans MS",15, "bold"))
        self.label.place(relx=0.5, y=30, anchor=CENTER)
        self.txt_input = Text(root, width=45, height=5, font='Arial 12 bold')
        self.txt_input.place(relx=0.5, y=100, anchor=CENTER)

        ttk.Style().configure("TButton", font=("Helvetica",12, "bold"), padding=6, relief="flat", background="blue", foreground="red")
        self.btn_translate = Button(root, width=45,text="Перевести", command=self.translate)
        self.btn_translate.place(relx=0.5, y=180, anchor=CENTER)

        self.txt_translate = Text(root, width=45, height=5, font='Arial 12 bold')
        self.txt_translate.place(relx=0.5, y=260, anchor=CENTER)
    

    def translate(self):
        self.text = self.txt_input.get('1.0', END)
        self.a = translator.translate(self.text, dest='ru')    
        self.txt_translate.delete('1.0', END)
        self.txt_translate.insert('1.0', self.a.text)


if __name__ == '__main__':
    root = Tk()    
    root.geometry("600x400")
    root.title("demonstalkerTranslate, version: 1.0")
    root.resizable(width=False, height=False)
    root['bg'] = 'black'
    translator = Translator()
    app = App(root)
    root.mainloop() 