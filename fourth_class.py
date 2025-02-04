def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))


if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

student = {"name" : "alice", "age" : 25, "grade" : "A"}
print(student["name"])
print(student["age"])
student["major"] = "physics"
print(student)
del student["grade"]
print(student)
for key, value in student.items():
    print(f"{key} : {value}")

i = 1
while i <= 5:
    print(i)
    i += 1
var = 7
while var > 0:
    print("Current variable value:", var)   
    var = var-1
    if var == 3:
        break
    else:
        if var == 5:
            var = var - 1
            continue
    print("Good Work")