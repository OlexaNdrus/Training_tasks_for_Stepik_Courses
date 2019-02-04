sample,a,b = (input() for i in range(3))

def replacer(sample,a,b):
    counter=0
    while counter<1000:
        if a in sample:
            sample=sample.replace(a,b)
            counter+=1
        else:
            return counter
    return 'Impossible'

print(replacer(sample,a,b))
