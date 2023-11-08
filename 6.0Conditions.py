x = 149
if x >= 150:
    print('selected')
else:
    print('Not selected')

# ternary operator
msg = 'You are a ' + ("Security" if x >= 150 else "Labour")
print(msg)

marks = 36

if marks < 0 or marks > 100:
    print('Invalid')
    exit()
    #break
elif marks >= 0 and marks <= 35:
    print('W')
elif marks < 55:
    print('S')
elif marks < 65:
    print('C')
elif marks < 75:
    print('B')
elif marks <= 100:
    print('A')


