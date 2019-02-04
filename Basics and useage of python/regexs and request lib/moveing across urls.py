import requests,re

try:
    URL_a=input()
    resa=requests.get(URL_a)
    print(resa)
except:
    print('No')

try:
    URL_b=input()
    resb=requests.get(URL_b)
except:
    print('No')

anwer='No'
for url in re.finditer(r'href="(.+)"', resa.text):
    res = requests.get(url.group(1))
    if f'<a href="{URL_b}"' in res.text:
        anwer='Yes'
        break
print(anwer)
