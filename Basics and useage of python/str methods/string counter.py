a,b = (input() for i in range(2))
counter=0

while b in a:
    a=a[a.find(b)+1:]
    counter+=1

print(counter)