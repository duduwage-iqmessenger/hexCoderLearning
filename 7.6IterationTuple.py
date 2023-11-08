d = ("A", "B", "D", "C")

# Method 1 to print keys and values of the dictionary
for k in d:
#    val = d[k]
    print(k)
# Method 2 to print keys and values of the dictionary
#for _key, _val in d.items():
#    print(_key, _val)
# Method 1 to print keys and values of the dictonary
for __key, __val in enumerate(d):
    print(__key, __val)
