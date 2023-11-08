# def get_odd_numbers(upper_limit):
#    odd = []
#    for i in range(0, upper_limit):
#        if i % 2 == 1:
#            print('Odd', i)
#            odd.append(i)
#
#    return odd
#
# print('- start -')
# x = get_odd_numbers(10)
# print('- end -')
# print(x)

def get_odd_numbers(upper_limit):
    #    odd = []
    for i in range(0, upper_limit):
        if i % 2 == 1:
            print('Odd', i)
            yield i


#    return odd

print('- start -')
x = get_odd_numbers(10)
print('- end -')

for i in x:
    print('Loop', i)
print(x)
