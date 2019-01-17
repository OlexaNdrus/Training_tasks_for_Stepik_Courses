mro_obj={}
for i in range(int(input())):
    info=input().split(' : ')
    if len(info)>1:
        if len(info[1])>1:
            for i in info[1].split():
                info.append(i)
            del info[1]
        mro_obj[info[0]]=info[1:]

def MRO_rec(child):
    global parents
    if child in mro_obj.keys() :
        [parents.append(i) for i in mro_obj[child]]
        for i in mro_obj[child]:
            MRO_rec(i)

for i in range(int(input())):
    info=input().split()
    parents,pos_parent=[],info[0]
    MRO_rec(info[1])
    if pos_parent in parents or pos_parent==info[1]:
        print('Yes')
    else:
        print('No')