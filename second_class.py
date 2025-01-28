print("Albert Einstein once said")
print('Albert Einstein once said')

print("*")
print("**")
print("***")
print("****")

print("Addition : 5+3 = ", 5+3)
print("Addition : 5-3 = ", 5-3)
print("Addition : 5*3 = ", 5*3)
print("Addition : 5/3 = ", 5/3)

print("Using \ for new line")
print("Using \\ for new line")
print("First Line\nSecond Line")
print("\nUsing \\t for a tab")
print("Column1\tColumn2\nColumn3")
print("\nusing \\\* for quotes")
print("He said, \"Python is awesome!\"")

print("Name\tAge\tCity")
print("Alice\t25\tLondon")
print("Bob\t30\tNYC")

print("Hello", "World", end = '###')
print("Bye", "World", sep = '$$')

message = "GOOD DAY"
print(message)

#1. Variable names can contain only letters, numbers, and underscores.
#2.⁠ ⁠They can start with a letter or an underscore, but not with a number.
#3.⁠ ⁠Spaces are not allowed in variable names, but underscores can be used to separate word
#4.⁠ ⁠Avoid using Python keywords and function names as variable Names
#5.⁠ ⁠Variable names should be short but descriptive.
# For example, name is better than n, student_name is better than s_n
#6. Be careful when using the lowercase letter l and the uppercase letter O because they
#7.⁠ ⁠reserved words (35)cannot be used as variable names and, as, assert,
# break, class, continue, def, del, elif, else, except, False
# if, import, in, is, lambda, None, nonlocal, not, or, pass

msg = "GOOD DAY"
print(msg.title())
print(msg.lower())
print(msg.upper())
print(msg.swapcase())

msg2 = "  GOOD  "
print(msg2.strip())
print(msg2.lstrip())
print(msg2.rstrip())

a = 1000
b = 1_0_00
print(a)
print(b)

a = "rose"
b = "beautiful"
c = f'{a} is a {b} flower'
print(c)
c = f'{a.title()} is a {b} flower'
print(c)

a = 10.5
b = 4.2
print("Add:", a+b)
print("Sub:", a-b)
print("Mul:", a*b)
print("Div:", a/b)

z1 = 2+3j
z2 = 1+2j
print("Add:", z1+z2)
print("Sub:", z1-z2)
print("Mul:", z1*z2)
print("Div:", z1/z2)
print("Real part of z1:", z1.real)
print("Imaginary of part of z1:", z1.imag)