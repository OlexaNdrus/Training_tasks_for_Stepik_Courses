import requests,sys

numbers=[]
for line in sys.stdin:
    numbers.append(line.rstrip())

type='math'
api_url='http://numbersapi.com'
headers = {'Content-type': 'application/json'}

for num in numbers:
    full_url='/'.join((api_url,num,type))
    response_json=requests.get(full_url,headers=headers).json()
    if response_json['found']:
        print('Interesting')
    else:
        print('Boring')


