x = {"Hello", "World", "Hello", 1, "1"}
y = {"x", "y", "12"}
print("x ", x)

print(x | y)  # Adding two sets

# z = (x | y)
z = x.union(y)  # Adding two sets
print("z ", z)

print(type(z))
z.add("WorlD")

print("z ", z)
# x.add("WorlD")
# x.add("world")
print(z.add("world"))
print(z)
print("x ", x)

print("x - y ", x-y)
