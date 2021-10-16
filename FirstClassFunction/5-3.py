def reverse(word):
    return word[::-1]


fruits = ['strawberry', 'fig', 'apple']
print(reverse("testing"))
fruits = sorted(fruits, key=reverse)
print(fruits)
