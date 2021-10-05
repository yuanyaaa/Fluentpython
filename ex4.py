def make_avg():
    count = 0
    total = 0

    def avg(new_value):
        # nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return avg

avg = make_avg()
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)

avg(10)