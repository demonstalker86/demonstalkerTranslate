import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'ZjJmYTY3ZTQtZjA3OS00MzljLWJhODctYTkzNmIxZGZjNjdiOjBiNmYwM2VjMGY5YzRhZTZiZjRjMDZkYTM1YWI4OTRi'

headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

if auth.status_code == 200:
    token = auth.text
    while True:
        a = input('Хотите перевести слово с английского на русский, иначе будет обратно? [yes/нет]: ')
        if a == 'yes':
            word = input('Введите слово для перевода: \n')        
            if word:
                headers_translate = {'Authorization': 'Bearer ' + token}
                params = {'text': word, 'srcLang': 1033,  'dstLang': 1049}           
                r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
                res = r.json()
                try:
                   print(res['Translation']['Translation'])
                except:
                   print('Не найдено варианта для перевода')        
        elif a == "нет":
               word = input('Введите слово для перевода: \n')        
               if word:
                  headers_translate = {'Authorization': 'Bearer ' + token}
                  params = {'text': word, 'srcLang': 1049,  'dstLang': 1033}           
                  r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
                  res = r.json()
                  try:
                     print(res['Translation']['Translation'])
                  except:
                     print('Не найдено варианта для перевода')            
else:
    print('Error!')
