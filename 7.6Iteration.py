d = {
    "A": 1,
    "B": 3,
    "D": 4,
    "C": 2
}

# Method 1 to print keys and values of the dictionary
for k in d:
    val = d[k]
    print(k, val)

# Method 2 to print keys and values of the dictionary
for _key, _val in d.items():
    print(_key, _val)

# Method 3 to print keys and values of the dictionary
for __key, __val in enumerate(d.items()):
    print("\n", __key, __val)
    lttr, num = __val
    print(__key, lttr, num)
