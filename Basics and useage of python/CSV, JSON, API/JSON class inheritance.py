import json

data = json.loads(input())
dicty={}

def recur(heir,list):
    for j in list:
        checker(j,heir)
        for i in data:
            if j==i["name"]:
                recur(heir,i["parents"])

def checker(parent,child):
    if parent not in dicty.keys():
        dicty[parent] = [child]
    else:
        dicty[parent].append(child)

for i in data:
    checker(i['name'], i['name'])
    recur(i['name'], i['parents'])

for i in sorted(dicty):
    print(i,':',len(set(dicty[i])))

