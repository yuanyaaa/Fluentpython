def f(a, b):
    a += b
    return a


x, y = 1, 2
print(f(x, y))
print((x, y))

x, y = [1, 2], [3, 4]
print(f(x, y))
print((x, y))
x, y = (1, 2), (3, 4)
print(f(x, y))
print((x, y))

