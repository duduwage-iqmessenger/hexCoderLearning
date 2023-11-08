# x = [12, 13, 14, 15, 16, 17, 18, 19, 20]

# count = 0

# while count <= len(x) - 1:
# print("x ", x[count])
# count += 1


# x = [12, 13, 14, 15, 16, 17, 18, 19, 20]
# c = 0

# while True:
# if c == len(x):
# break
# print("c ", x[c])
# c += 1

# x = [12, 3, 67, 123, -88]

# oddNum = evenNum = ""
# for num in x:
#    if num%2 == 0:
#        evenNum += "|" + str(num)
#    else:
#        oddNum += "|" + str(num)
# print(evenNum, end="|")
# print(oddNum, end="|")
# print()

# oddNum = evenNum = None
# for num in x:
# if num % 2 == 0:
# continue
# else:
# oddNum += "|" + str(num)
# evenNum += "|" + str(num)

# print(evenNum, end="|")
# print()
# print(oddNum, end="|")
# print()
# count = 0
# while count < 5:
#    print("count ", count)
#    count += 1

# count = 0
# while True:
#    if count == 5:
#        break
#    print("count ", count)
#    count += 1
# index = 0
# for i in x:

# if i < 0:
#    break
# print(i)
# index += 1

# use of continue and break keywords

# x = [13, 12, 23, 567, 123, 88]

# count = 0 # iterate ten times and use break

# while True:

#    print('count ', count)
#    count += 1
#    if count == 10:
#        break

# x = [-12, -23, -567, -123, 8] # print the number and Odd/Even in the list, use continue

# count = 0

# while count <= len(x)-1:
#    i = x[count]
#    if i % 2 == 0:
#        print("Even \t", i)
#        count += 1
#        continue
#    print("Odd \t", i)
#    count += 1

x = [-12, -23, -567, -123, 8]  # print the number and Odd/Even in the list, use continue and break

count = 0

while True:

    if count > len(x) - 1:
        break

    i = x[count]

    if i % 2 == 0:
        print("Even \t", i)
        count += 1
        continue
    print("Odd \t", i)
    count += 1
