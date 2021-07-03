import requests
from tkinter import *
from tkinter.ttk import *
from functools import partial

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'ZjJmYTY3ZTQtZjA3OS00MzljLWJhODctYTkzNmIxZGZjNjdiOjBiNmYwM2VjMGY5YzRhZTZiZjRjMDZkYTM1YWI4OTRi'

headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

def Translate(headers_auth, auth):
    auth.status_code =200         
    token = auth.text
    word = txt.get()    
    if var.get() == 0:
        headers_translate = {'Authorization': 'Bearer ' + token}
        params = {'text': word, 'srcLang': 1033,  'dstLang': 1049}           
        r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
        res = r.json()
        label.configure(text=res['Translation']['Translation'])            
        try:
            print(res['Translation']['Translation'])
        except:
            print('Не найдено варианта для перевода')    
    elif var.get() == 1:
        headers_translate = {'Authorization': 'Bearer ' + token}
        params = {'text': word, 'srcLang': 1049,  'dstLang': 1033}           
        r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
        res = r.json()
        label.configure(text=res['Translation']['Translation'])
        try:
            print(res['Translation']['Translation'])
        except:
            print('Не найдено варианта для перевода')


window = Tk()
window.title("demonstalkerTranslate")
window.geometry("800x600")
var = IntVar()
var.set(0)
btn_translate_er = Radiobutton(window, text='С английского на русский',variable=var, value=0)
btn_translate_er.grid(column=0, row=0)
btn_translate_re = Radiobutton(window, text='С русского на английский',variable=var, value=1)
btn_translate_re.grid(column=2, row=0)

txt = Entry(window,width=20)
txt.grid(column=4,row=0)
btn_translate = Button(window, text="Перевести",command=partial(Translate,headers_auth, auth))
btn_translate.grid(column=5, row=0)
label = Label(window, text="Здесь будет перевод",font=("Comic Sans MS",24, "bold"))
label.grid(column=0,row=1)
window.mainloop() 