from array import array
import math



class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        print("iter!!!")
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        print("str!!!")
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, format_spec):
        components = (format(i, format_spec) for i in self)
        return '({}, {})'.format(*components)


v1 = Vector2d(3, 4)
# x, y = v1
# print(x, y)
# print(v1)
# print(repr(v1))
print(format(v1, '.3e'))
