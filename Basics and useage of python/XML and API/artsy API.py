import requests,sys,json

client_id='5d17f2938be0c659e030'
client_secret='b1eec450d8d846186970914f4183f928'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

j = json.loads(r.text)
token = j["token"]


artists=[]
for line in sys.stdin:
    artists.append(line.rstrip())
headers = {"X-Xapp-Token" : token}
artists_dict = {}
for art in artists:
    url='/'.join(("https://api.artsy.net/api/artists",art))
    r = requests.get(url, headers=headers)
    j = json.loads(r.text)
    artists_dict[j['birthday']] = j['sortable_name']



with open("file","w",encoding="utf-8") as f:
    for i in sorted(artists_dict.items()):
        f.write(i[1]+'\n')
        print(i)

# or i in sorted(artists_dict.items()):
#     print(i[1])