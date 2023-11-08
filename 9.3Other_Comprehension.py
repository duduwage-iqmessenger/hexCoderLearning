a = [12, 45, 85, 87, 33, 100, 34, 11]
b = []


def is_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


# create a dictionary list
b = {value: is_odd(value) for i, value in enumerate(a) if i % 2 == 0}

print(a)
print(type(b))
print(b)
