import requests
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from functools import partial
from tkinter import scrolledtext



URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'ZjJmYTY3ZTQtZjA3OS00MzljLWJhODctYTkzNmIxZGZjNjdiOjBiNmYwM2VjMGY5YzRhZTZiZjRjMDZkYTM1YWI4OTRi'

headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)


def Translate(headers_auth, auth):
    auth.status_code =200         
    token = auth.text
    word = txt.get("1.0", 'end')    
    if var.get() == 0:
        headers_translate = {'Authorization': 'Bearer ' + token}
        params = {'prefix': word, 'srcLang': 1033,  'dstLang': 1049, 'pageSize': 20, 'StartPos': ''}           
        r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
        res = r.json()                    
        try:
              label.configure(text = res["Translation"]["Translation"])
        except RuntimeError:
              label.configure(text='Не найдено варианта для перевода')            
    elif var.get() == 1:
        headers_translate = {'Authorization': 'Bearer ' + token}
        params = {'prefix': word, 'srcLang': 1049,  'dstLang': 1033, 'pageSize': 20, 'StartPos': ''}           
        r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
        res = r.json()       
        try:
            label.configure(text = res["Translation"]["Translation"])
        except RuntimeError:
            label.configure(text='Не найдено варианта для перевода')
            

window = Tk()
window.title("demonstalkerTranslate")
window.geometry("800x400")
var = IntVar()
btn_translate_er = Radiobutton(window, text='С английского на русский',variable=var, value=0)
btn_translate_er.grid(column=0, row=0)
btn_translate_re = Radiobutton(window, text='С русского на английский',variable=var, value=1)
btn_translate_re.grid(column=1, row=0)

txt = scrolledtext.ScrolledText(window,width=30,height=10)
txt.insert(INSERT, 'Текстовое поле')
txt.grid(column=2,row=0)
ttk.Style().configure("TButton", font=("Helvetica",12, "bold"), padding=6, relief="flat", background="blue", foreground="red")
btn_translate = Button(window, text="Перевести", command=partial(Translate,headers_auth, auth))
btn_translate.grid(column=3, row=0)
ttk.Style().configure("TLabel", foreground="blue", background="orange")
label = Label(window, text="Здесь будет перевод", font=("Comic Sans MS",18, "bold"))
label.grid(column=0,row=3)
window.mainloop() 
