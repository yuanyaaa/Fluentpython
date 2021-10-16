import random


class BingoCage:
    # 确保类为可调用对象
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    # 确保可直接调用类的实例
    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(bingo())
print(bingo())
