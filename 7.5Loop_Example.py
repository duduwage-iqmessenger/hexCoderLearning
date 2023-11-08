# find min value and max value in a list [using for loop]
#x = [12, 13, 14, 15, 16, 17, 18, 19, 20]
#max = min = x[0]
#min = x[0]

#for i in x:
#    if max < i:
#        max = i
#    if min > i:
#        min = i

#print("Max \t:", max)
#print("Min \t:", min)

# find min value and max value in a list [using while loop]
x = [12, 13, 14, 15, 16, 17, 18, 19, 20]
max = min = x[0]
count = 0
while count < len(x):
    _val = x[count]
    if max < _val:
        max = _val
    if min > _val:
        min = _val
    count += 1
print("Max \t:", max)
print("Min \t:", min)