def mod_checker(x, mod=0):
    return lambda y: y % x == mod

if __name__=='__main__':
    checker_3 = mod_checker(3)
    print(checker_3(4))

