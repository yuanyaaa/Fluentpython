from typing import List, Tuple, Dict, Set


def clip(text: str, max_len: 'int > 0' = 80) -> str:
    """在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()


test = clip("dsafaf", max_len=10)
print(test)
test2 = clip("dsafaf", max_len=-1)
print(test2)

test3: int = 4
test4: int = 5.0

a1: List[int]  # a1是一个list，其中的数据都是int类型，没有赋值
a2: List[str] = ['1', '2', '3']  # a2是一个list，其中的数据都是int类型，赋值为['1','2','3']
b1: Tuple[int]  # a1是一个tuple，其中的数据都是int类型，没有赋值
b2: Tuple[str, int, float] = ("樱木花道", 18, 183.0)
c1: [Dict[str, int]] = {}  # c1是一个dict，其中key为str类型，value为int型，没有赋值
c2: [Dict[str, int]] = {'a': 1, 'b': 2, 'c': 3}  # c1是一个dict，其中key为str类型，value为int型，赋值为{'a':1, 'b':2, 'c':3}
d1: Set[int] = {1, 2, 3}
