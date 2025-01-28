x=[1,2,3,4]
print(sum(x))
print(max(x))
print(min(x))
print(len(x))
x.append(5)
print(x)
x.extend([6,7,8])
print(x)
x.insert(2,9)
print(x)
x.remove(9)
print(x)
x.pop(0)
print(x)
x.clear()
print(x)
x=[1,2,3,4]
print(x.index(3))
print(x.count(3))
x=[1,4,3,2]
x.sort()
print(x)
x.reverse()
print(x)
y=x.copy()
print(y)



my_list = [1, 2, 3, 4, 5]
removed_element = my_list.pop(2) 
print(my_list) 
print(removed_element)

my_list.remove(4)  
print(my_list)


my_list = [10, 20, 30, 40, 50]
del my_list[2]  
print(my_list)  

my_list.remove(40) 
print(my_list) 
del my_list  


my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

my_list.insert(1, 10) 
print(my_list) 

num1 = 5
num2 = 25
print("Number: %d" % num1)

print("Number: %2d" % num1)
print("Number: %2d" % num2)