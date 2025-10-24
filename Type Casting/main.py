# Implicit and Explicit Type Conversion

# Implicit Type
a = 5
b = 6.2

print("Type of variable a: ", type(a))
print("Type of variable b: ", type(b))

c = a + b
print("Type of variable c: ", type(c))

print(a)
print(b)
print(c)

# Explicit Type
num1 = "10"
num2 = 20

print("Type of variable num1: ", type(num1))
print("Type of variable num2: ", type(num2))

# Operation 1
print(int(num1) + num2)
print(type(int(num1) + num2))

# Operation 2
print(str(int(num1) + num2))
print(type(str(int(num1) + num2)))