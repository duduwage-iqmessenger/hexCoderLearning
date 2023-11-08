def get_grades(marks, subject="Unknown"): # Posistional and Default arguments
    print("Subject ", subject)
    if marks < 0 or marks > 100:
        print('Invalid')
        exit()
        # break
    elif marks >= 0 and marks <= 35:  # elif 0 <= marks <= 35:
        print('W')
    elif marks < 55:
        print('S')
    elif marks < 65:
        print('C')
    elif marks < 75:
        print('B')
    elif marks <= 100:
        print('A')


#get_grades(75, "Maths")
#get_grades(80)

# Argument types in functions
# positional
# default
# named
# packed
# keyword arguments

#marks = [10, 20, 30]


def printtot(*marks):
    print(type(marks))
    print(marks)
    tot = 0
    for i in marks:
        tot += i
    print(tot)



printtot(10, 20, 30) # Packed