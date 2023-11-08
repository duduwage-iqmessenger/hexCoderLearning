# var1 = {'10000': 'Colombo', '123': 'Kaluthara', '555': 'Galle'}
# print(var1)
# print(var1.keys())
# print(var1.values())
# print(var1.get('1233', ' Notfound'))
# var1['420'] = 'Kandy'
# print(var1)
# del var1['420']
# print(var1.keys())
# print(var1.values())

# s = {"Hello", "World", "How", "are", "you", "?"}
# t = {"?", "!"}

# print(s.union(t))
# print(s | t)
# print(s - t)

x = {
    'a': ['Hello', 'Hi', 'Good morning'],
    'b': ['Bye', 'Good night'],
    "c": 16
}

y = x['a']
y.append('Aayubowan')

z = x["c"]
z = 17

print(x)
print(z)
