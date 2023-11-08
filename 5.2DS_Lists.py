x = [10, 11, 12, 13]
y = [1, 2, 'c', 4]

_x = x + y
_x[3] = 555
_x.append(77)
print(_x)

_x.insert(1, 99)

# _x[10] = 555
print(_x)

_x.pop(1)
print(_x)

print('c' not in _x)
print(len(_x))

# list slicing
print(x[0:3])  # 10, 11, 12
print(x[2:6])  # 12, 13
print(x[2:])  # 12,13
print(x[:])  # entire list
print(x[:6])  # entire list
print(x) # entire list
print(x[:-1]) # starting from the beginning till last excluding
print(x[-1]) # last element

print(type(x[:-1]))
print(type(x[-1]))
