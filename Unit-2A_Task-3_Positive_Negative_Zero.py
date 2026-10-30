# This program checks whether a given number is positive, negative, or zero.

num=int(input("Enter a number:"))
if num>0:                                           #if condition:
    print(f"The number {num} is positive.")
elif num<0:                                         #elif condition:
    print(f"The number {num} is negative.")
else:                                               #else condition:
    print(f"The number {num} is zero.")