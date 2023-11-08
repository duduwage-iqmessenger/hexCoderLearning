#== List ===
#x = [10, 12, 14, 16, 18]
#y = [10, 12, 14, 16, 18]

#print(x)
#print(x[0])
#print(len(x))

#x.append(20)
#print(x)

#x.insert(0, 8)
#print(x)

#x.remove(14)
#print(x)

#x.pop(0)
#print(x)

#print(x + y)
#is_10_in_xy = 10 in x+y
#print(is_10_in_xy)

#is_8_in_xy = 8 not in x+y
#print(is_10_in_xy)

# === Dictionary ===
#d = {"1": "a", "2": "b", "3": "c", "4": "d"}
#d["5"] = "e"
#d["6"] = "a"

#print(d)
#print(len(d))
#print(d.keys())
#print(d.values())

#print(d.get("1","Not there"))
#print(d.get("7","Not there"))

#del d["6"]
#print(d.keys())
#print(d.values())

#d.clear()
#print(d.keys())
#print(d.values())

# ==== Pass by reference & Pass by value
#x = {
#    1 : "Hello",
#    2 : "How",
#    3 : ["Are","Pass","by","reference"],
#    4 : "You",
#    5 : 5
#}
#print("print x ",x)
#y = x[3]
#print("print y ", y)

#y.append("Example")

#print("print y ", y)
#print("print x ", x)
#z = x[5]
#z += 5
#print("print z ", z)
#print("print x ", x)

### === Sets === ###

#x = {'Hello', 'World', 'Hello', '1', "2", '1'}
#y = {'3', '2', '1', 'funny', 'reptilian'}
#print("print x ", x)
#x.remove('1')
#print("print x after remove ", x)
#print(x.union(y))
#print(y | x)
#print(x - y)
#print('1' in y)

## === Tuple === ##

#tupleT = ('reptilian', 'Hello', '1', 'funny', '3', 'World', '2', '2')
#print("count ", len(tupleT))
#print("type ", type(tupleT))
##print("print ", tupleT)
#print("print element 0 ", tupleT[0])
#print("print count of 2 ", tupleT.count('4'))

# unpacking tuple
unpackTupleT = ('reptilian', 'Hello', 'funny', 'World')
p1, p2, p3, p4 = unpackTupleT
print(p2,p3,p1)
print("<",p2,p3,p1,">", sep="|")
print("<","Where", "are", "the", "spaces", sep="",end=">")