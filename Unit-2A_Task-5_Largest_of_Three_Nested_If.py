# Program to find the largest of three numbers using nested if statements :
x = int(input("Enter the first number: "))  
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))
if x>=y:
    if x>=z:
        largest = x
    else:
        largest = z
else:
    if y>=z:
        largest = y
    else:
        largest = z
print(f"Largest={largest} (among {x}, {y}, and {z})")