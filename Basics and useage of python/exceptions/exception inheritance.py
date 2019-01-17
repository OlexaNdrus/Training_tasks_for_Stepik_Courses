mro_obj = {}
list_for_print,result = [],[]
for i in range(int(input())):
    info = input().split(' : ')
    if len(info) > 1:
        parents = info[1].split()
        mro_obj[info[0]] = parents
    else:
        mro_obj[info[0]] = []

def recur(exception):
    exc_parents = mro_obj[exception]
    global exc
    if exc_parents:
        for parent in exc_parents:
            if parent in mro_obj.keys():
                recur(parent)
            else:
                list_for_print.append(exc)
                break

for i in range(int(input())):
    exc = input()
    if exc in mro_obj.keys() and exc not in list_for_print:
        recur(exc)
        del mro_obj[exc]
[result.append(i) for i in list_for_print if not result.count(i)]
print(*result, sep='\n')