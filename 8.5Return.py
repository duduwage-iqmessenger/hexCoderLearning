
def get_grade(marks, subject=None):
    returnval = None
    #print('Subject ', subject)
    if not subject:
        return 'Subject NOT included'
    if marks < 0 or marks > 100:
        return 'Invalid marks'
    elif marks < 35:
        returnval = 'W'
    elif marks < 55:
        returnval = 'S'
    elif marks < 65:
        returnval = 'C'
    elif marks < 75:
        returnval = 'B'
    else:
        returnval = 'A'
    return subject, returnval

def print_grades(g):
    # print(len(g))
    if len(g) == 1:
        print('Grade ', g)
    else:
        print(g)


print(get_grade(-75, 'Sinhala'))
#grade = get_grade(-75, 'Sinhala')
#print_grades(grade)
# print('-75', 'Sinhala ')

marks = 17

grade = get_grade(marks)
print_grades(grade)

print_grades(get_grade(85, 'Science'))
subject, grade = get_grade(45, 'Art')
print(subject, grade)
