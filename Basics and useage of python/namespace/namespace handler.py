num_rows=int(input())
vars_in_namesp,namespaces={},{}
vars_in_namesp['global'] = []
for i in range(num_rows):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        if arg not in namespaces:
            namespaces[arg] = []
        namespaces[arg].append(namesp)
        vars_in_namesp[namesp] = []
    elif cmd == 'add':
        vars_in_namesp[namesp].append(arg)
    else:
        while True:
            if arg not in vars_in_namesp[namesp]:
                if namesp=='global':
                    print(None)
                    break
                for key, value in namespaces.items():
                    if namesp in value:
                        namesp=key
                        break
            else:
                print(namesp)
                break