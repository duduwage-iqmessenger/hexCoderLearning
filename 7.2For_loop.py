x = [12, 13, 14, 15, 16, 17, 18, 19, 20]

i = 0
for item in x:
    # print(x[i])
    # print("i ", i, item)
    print(i, "-", item)
    i += 1

for key, val in enumerate(x):
    print(key, "--", val)

for item in range(1,3):
    print(item)

r = range(0, len(x))

for _item in r:
    print(x[_item])

    x = [12, 23, 567, 123, 88]

    # index = 0

    # for item in x:
    # y = x[index]
    # print(index, x[index])
    # index +=1

    for index, value in enumerate(x):
        # print(type(item), item)
        # index, value = 0, 0
        # index = item[0]
        # value = item[1]
        print(index, value)

    rangeR = range(0, len(x))
    print(type(rangeR))

    for item in rangeR:
        print(item, x[item])
