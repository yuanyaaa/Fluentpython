from dis import dis

b = 6


def f1(a):
    print(a)
    print(b)


def f2(a):
    print(a)
    print(b)
    b = 9


def f3(a):
    global b
    print(a)
    print(b)
    b = 9


f1(1)
dis(f1)
# f2(2)
dis(f2)
f3(3)
dis(f3)
