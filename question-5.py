#create a python class called bank account which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance
class BankAccount:
    def __init__(self, account_number: int, name: str, balance: float = 0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount: float):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient balance or invalid amount.")
    
    def get_balance(self):
        return self.balance
    
    def display_info(self):
        print(f"Account Number: {self.account_number}\nAccount Holder: {self.name}\nBalance: ${self.balance:.2f}")

#create a constructor with parameters: accountNumber, name, balance.
class BankAccount:
    def __init__(self, accountNumber: int, name: str, balance: float):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

#Create a Deposit() method which manages the deposit actions.
def deposit(self, amount: float):
    if amount > 0:
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
    else:
        print("Deposit amount must be positive.")



#create a rectangular class in python language allowing you build a rectangle with length and width attributes.
class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def display_info(self):
        print(f"Rectangle: Length = {self.length}, Width = {self.width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

#create a perimeter method to calculate the perimeter of rectangle and area method to calculate the area of a rectangle.
def area(self):
    return self.length * self.width
def perimeter(self):
    return 2 * (self.length + self.width)

#create a method display() that displays the length, width, perimeter and area of the rectangle.
def display(self):
    print(f"Rectangle: Length = {self.length}, Width = {self.width}")
    print(f"Area: {self.area()}")
    print(f"Perimeter: {self.perimeter()}")

#create a parallelepipede child class inhertingfrom rectangle class and with height attribute and a volume method.
class Parallelepiped(Rectangle):
    def __init__(self, length: float, width: float, height: float):
        super().__init__(length, width)
        self.height = height
    
    def volume(self):
        return self.length * self.width * self.height
    
    def display(self):
        super().display()
        print(f"Height: {self.height}")
        print(f"Volume: {self.volume()}")

# 1. What are python's key features that makes it popular for programming
# Python is a high-level, interpreted, and general-purpose programming language that emphasizes code readability and simplicity. It is widely used for web development, scientific computing, data analysis, artificial intelligence, and more. Some key features that make Python popular for programming include:
# 2. What is difference between mutable and immutable types with examples
# Mutable types in Python can be changed after they are created, while immutable types cannot be changed. Mutable types include lists, dictionaries, and sets, while immutable types include strings, tuples, and numbers. For example:
# 3. What is the difference between a list and a tuple
# A list is a mutable data structure in Python that can be changed after it is created, while a tuple is an immutable data structure that cannot be changed. Lists are created using square brackets [], while tuples are created using parentheses (). For example:
# 4. What are python's conditional statements and how are they used?
# Python's conditional statements are used to make decisions in a program based on certain conditions. The main conditional statements in Python are if, elif, and else. The if statement is used to execute a block of code if a condition is true, while the elif statement is used to check additional conditions. The else statement is used to execute a block of code if none of the conditions are true. For example:
# 5. Write a python program if a number is even or odd
# 6. Write a python program to find factorial of a number using for loop
# 7. Write a python program to print a fibonacci series upto n terms
# 8. Write a python program to check if a number is palindrome or not
# 9. Write a python program to calculate roots of a quadratic equation
# 10. Write a python program to find fibonacci series using matrix exponentiation