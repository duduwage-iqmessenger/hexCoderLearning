# a = [12, 45, 85, 87, 33]

# b = a
# b.append(10)

# print(a)
# print(b)
# print('a ', type(a))
# print('a ', id(a))
# print('b ', id(b))

# creating a new list from an existing list (01)

# a = [12, 45, 85, 87, 33]
# b = list(a)

# print('a -',a)
# print('b -',b)

# print('a ', id(a))
# print('b ', id(b))

# creating a new list from an existing list [for loop] (02)
# a = [12, 45, 85, 87, 33]
# b =[] #empty list

# for i in a:
#    b.append(i)

# print('a ', id(a))
# print('b ', id(b))

# print('a -', a)
# print('b -', b)

# creating a new list from an existing list [comprehension] (02)
a = [12, 45, 85, 87, 33]
b = []  # create empty list

b.append(100)

print('a -', a)
print('b -', b)

print('a ', id(a))
print('b ', id(b))

print('a -', a)
print('b -', b)


def is_odd(number):
    # if number % 2 == 0:
    #    return True
    # else:
    #    return False

    # if number % 2 == 0:
    #    return True
    # return False

    # return number % 2 == 0
    return "Even" if number % 2 == 0 else "Odd"


b = [is_odd(i) for i in a]

print('a -', a)
print('b -', b)
