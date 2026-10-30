# Example solution: multiplication table using a for loop
number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    product = number * multiplier
    print(f"{number} x {multiplier} = {product}")