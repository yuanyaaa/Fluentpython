def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)

# 别名
fact = factorial
# 生成对象的帮助文档
# print(factorial.__doc__)
help(factorial)
# 类型
# print(type(fact))
# 采用map，把第一个参数应用到第二个参数的各个元素上得到的结果
# print(list(map(fact, range(11))))
