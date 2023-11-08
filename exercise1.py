x = [121, 23, 567, 123, 88, 568, 5]

_val = 0
_med = 0

for index, val in enumerate(x):
    _val = _val + val

_med = _val/(index+1)
print("my total ", _val)
print("my median ", _med)

tot = 0
median = 0
for i in x:
    tot += i

median = tot / len(x)

print("total ", tot)
print("median ", median)

maxValue = 0
for i in x:
    if i > maxValue:
        maxValue = i
print("Max Value in ", maxValue)

minValue = x[0]
for i in x:
    if i > minValue:
        pass
    else:
        minValue = i
print("Min Value in ", minValue)
