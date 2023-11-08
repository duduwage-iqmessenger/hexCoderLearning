a = [12, 45, 85, 87, 33, 100, 34, 11,12]
#b = []


def is_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


# by using comprehension
# b = [is_odd(value) for i, value in enumerate(a) if i % 2 == 0]

# create a dictionary list
#b = [{value: is_odd(value)} for i, value in enumerate(a) if i % 2 == 0]

# create a dictionary
#b = {value: is_odd(value) for i, value in enumerate(a) if i % 2 == 0}

# create a set
#b = {value for i, value in enumerate(a) if i % 2 == 0}

# create a tuple
b = (value for i, value in enumerate(a) if i % 2 == 0)

for i in b:
    print(i)

# same using for loop
# for i, value in enumerate(a):
#    if i % 2 == 0:
#        r = is_odd(value)
#        b.append(r)

print(a)
print(type(b))
print(b)
