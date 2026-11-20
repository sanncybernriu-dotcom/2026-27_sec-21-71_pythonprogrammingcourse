#UNIT-3D-TASK 14 GCD USIG RECURSION 
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
x, y = 48, 18
print("GCD:", gcd(x, y)) 