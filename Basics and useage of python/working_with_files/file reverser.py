with open('info.txt','r') as file, open('result.txt','a') as result:
    a=file.readlines()
    a[-1]+='\n'
    for i in reversed(a):
        result.write(i)
