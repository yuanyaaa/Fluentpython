def dec(func):
    def inner():
        print("inner!!!")

    return inner


@dec
def target():
    print("target!!!")


target()
print(target)
