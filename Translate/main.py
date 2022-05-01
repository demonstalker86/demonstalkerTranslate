"""Переводчик demonstalkerTranslate"""
from tkinter import ttk, Text, IntVar, INSERT, Tk

from tkinter.ttk import Radiobutton, Label, Button

from functools import partial

import requests

from сonfig import Key




URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = Key

headers_auth = {'Authorization': 'Basic ' + KEY}
auth_post = requests.post(URL_AUTH, headers=headers_auth)


def word_translate(auth):
    """Функция word_translate"""
    auth = auth_post
    auth.status_code = 200
    token = auth.text
    word = txt.get("1.0", 'end')
    if var.get() == 0:
        headers_translate = {'Authorization': 'Bearer ' + token}
        params = {'text': word, 'srcLang': 1033, 'dstLang': 1049}
        res_get = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
        res = res_get.json()
        try:
            label.configure(text = res["Translation"]["Translation"])
        except RuntimeError:
            label.configure(text = 'Не найдено варианта для перевода')
    elif var.get() == 1:
        headers_translate = {'Authorization': 'Bearer ' + token}
        params = {'text': word, 'srcLang': 1049, 'dstLang': 1033}
        res_get = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
        res = res_get.json()
        try:
            label.configure(text = res["Translation"]["Translation"])
        except RuntimeError:
            label.configure(text = 'Не найдено варианта для перевода')

window = Tk()
window.title("demonstalkerTranslate")
window.geometry("600x300")
var = IntVar()
btn_translate_er = Radiobutton(window, text='С английского на русский',variable=var, value=0)
btn_translate_er.grid(column=0, row=0)
btn_translate_re = Radiobutton(window, text='С русского на английский',variable=var, value=1)
btn_translate_re.grid(column=1, row=0)

txt = Text(window,width=20,height=5)
txt.insert(INSERT, 'Введите слово')
txt.grid(column=2,row=0)
ttk.Style().configure("TButton", font=("Helvetica",12, "bold"),
                     padding=6, relief="flat", background="blue", foreground="red")
btn_translate = Button(window, text="Перевести", command=partial(word_translate, auth_post))
btn_translate.grid(column=2, row=5)
ttk.Style().configure("TLabel", foreground="blue", background="orange")
label = Label(window, text="Здесь будет перевод", font=("Comic Sans MS",14, "bold"))
label.grid(column=0,row=3)
window.mainloop()
