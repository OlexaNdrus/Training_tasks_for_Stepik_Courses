import itertools

def checker(num):
    for i in range(2,round(pow(num, 0.5))+1):
        if num % i == 0:
            return False
    return True

def primes():
    start_num = 2
    while True:
        if checker(start_num):
            yield start_num
        start_num+=1

if __name__=='__main__':
    print(list(itertools.takewhile(lambda x : x <= 31, primes())))

