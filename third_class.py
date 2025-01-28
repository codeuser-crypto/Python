list = ['A', 'B', 'C', 'D']
print(type(list))
list.insert(2, 'X')
print(list)
list.append('Z')
print(list)
print(list[1:3])
print(list[:4])
print(list[4:])
print(list[-4:-1])
print(list[-1])

list[1] = 'Z'
print(list)
list[1:3] = ['X', 'Y']
print(list)

list1 = ['A', 'B', 'C']
list2 = ['X', 'Y', 'Z']
list1.extend(list2)
print(list1)

del list1[1]
print(list1)

list1 = ['A', 'B', 'C']
tuple = ['X', 'Y', 'Z']
list1.extend(tuple)
print(list1)

list1.remove('X')
print(list)
del list1[0]
print(list1)
list1.clear()
print(list1)