class multifilter:

    def judge_half(pos, neg):
        # allows element, if allows half of functions(pos >= neg)
        if pos >= neg:
            return True

    def judge_any(pos, neg):
        # allows element, if allows at least one of functions (pos >= 1)
        if pos >= 1:
            return True

    def judge_all(pos, neg):
        # allows element, if allows all functions(neg == 0)
        if neg == 0:
            return True

    def __init__(self, iterable, *funcs, judge = judge_half):
        # iterable - initial sequance
        # funcs - allowing functions
        # judge - main rule
        self.iterable = iterable
        self.judge = judge
        self.funcs = funcs

    def __iter__(self):
        # returns iter object
        for i in self.iterable:
            pos, neg = 0, 0
            for j in self.funcs:
                if j(i):
                    pos+=1
                else:
                    neg+=1

            if self.judge(pos, neg):
                yield i

#test functions
def f1(x):
    return x % 2 == 0


def f2(x):
    return x % 3 == 0


def f3(x):
    return x % 4 == 0

#testing
lister=[1,2,3,4,5,6,7,8,9,10]
funcs=(f1,f2,f3)
a=multifilter(lister, *funcs,)
print("Here it is : ", type(a))
for i in a:
    print(i)
