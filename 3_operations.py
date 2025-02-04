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

for i in range(5,15):
    print("%2d is the number" %i)

for i in range(5,15):
    print("%1d is the number" %i)

x=int(input('enter x value'))
y=int(input('enter y value'))
z=x+y
print(z)

a=2
b=4
print(f"sum of {a} and {b} is {a+b}")
print(f"product of {a} and {b} is {a*b}")
print(f"quotient of {a} and {b} is {a/b}")
print(f"remainder of {a} and {b} is {a%b}")
print(f"{a} to the power of {b} is {a**b}")
print(f"floor division of {a} and {b} is {a//b}")
print(f"subtract {b} from {a} is {a-b}")
print(f"floor division of {b} and {a} is {b//a}")


p=True
q=False
print(f"p and q is {p and q}")
print(f"p or q is {p or q}")
print(f"not p is {not p}")
print(f"not q is {not q}")
print(f"p and not q is {p and not q}")
print(f"p or not q is {p or not q}")
print(f"not p and q is {not p and q}")
print(f"not p or q is {not p or q}")
print(f"not p and not q is {not p and not q}")
print(f"not p or not q is {not p or not q}")