import re,requests

domain_list=[]
pattern=re.compile(r'<a[\w\s=".]+href( )?=( )?["\']((http(s)?|ftp)?://)?((www[.])?(\w+([-_])*(\w)*[.])+\w+)([/:"\'])*',re.DOTALL)
file = requests.get(input()).text
res=re.findall(pattern,file)

for i in res:
    if i[5] not in domain_list:
        domain_list.append(i[5])

for i in sorted(domain_list):
    print(i)