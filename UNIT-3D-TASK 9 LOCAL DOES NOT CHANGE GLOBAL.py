# UNIT-3D-TASK 9 LOCAL DOES NOT CHANGE GLOBAL 
x = 10
def demo():
    x = 20  # local assignment
    print("Inside function, x =", x)
demo()
print("Outside function, x =", x)