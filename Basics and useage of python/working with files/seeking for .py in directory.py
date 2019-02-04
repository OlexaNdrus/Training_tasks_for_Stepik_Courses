import os

dir_strc=os.walk('main')

def py_file_checker(dir_strc):
    for i in dir_strc:
        for j in sorted(i[2]):
            if j.endswith('.py'):
                break
        yield i[0]

if __name__=='__main__':
    for i in py_file_checker(dir_strc):
        print(i)


