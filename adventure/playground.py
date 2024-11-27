def f2():
    print('>> f2()')
    f1()

def f1():
    print('>> f1()')
    10 / 0

f2()
