def keywordargs(**params):  # Keyword arguments
    print(type(params))
    if 'name' not in params:
        print("Error")
    else:
        print('Hello', params['name'])


keywordargs(age=45, city="Horana")
keywordargs(name="Damitha", age=60, city="Horana")

# Keyword arguments (kwargs)
#
#   in function call when key value pair is passed, converts kwargs to a dictionary
#   function(k1 = v1, k2 =v2, k3 = v3) -> def function (**kwargs):
#
#   in function call when a dictionary is passed, converts to kwargs
#   function(**dictionary) -> def function (k1, k2, k3):

kwargs = {
    'A': 1,
    'B': 2,
    'C': 3,
    'E': None
}


def pass_dict(A, B, C, E, D = 4):
    print(A, B, C, D, E)


pass_dict(**kwargs)
