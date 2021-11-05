from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from googletrans import Translator



def translater():
    text = txt_input.get('1.0', END)
    a = translator.translate(text, dest='ru')    
    txt_translate.delete('1.0', END)
    txt_translate.insert('1.0', a.text)




window = Tk()
window.geometry("600x400")
window.title("demonstalkerTranslate, version: 1.0")
window.resizable(width=False, height=False)
window['bg'] = 'black'
translator = Translator()

ttk.Style().configure("TLabel", foreground="white", background="black")
label = Label(window,  text="Введите текст на любом языке", font=("Comic Sans MS",15, "bold"))
label.place(relx=0.5, y=30, anchor=CENTER)
txt_input = Text(window, width=45, height=5, font='Arial 12 bold')
txt_input.place(relx=0.5, y=100, anchor=CENTER)

ttk.Style().configure("TButton", font=("Helvetica",12, "bold"), padding=6, relief="flat", background="blue", foreground="red")
btn_translate = Button(window, width=45,text="Перевести", command=translater)
btn_translate.place(relx=0.5, y=180, anchor=CENTER)

txt_translate = Text(window, width=45, height=5, font='Arial 12 bold')
txt_translate.place(relx=0.5, y=260, anchor=CENTER)


window.mainloop() 