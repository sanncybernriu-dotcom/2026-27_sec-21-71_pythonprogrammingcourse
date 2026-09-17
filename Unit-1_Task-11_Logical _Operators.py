  # python Logical Operators Exercises:
# Logical and opertor
a=5
result= a > 2 and a < 10                   #TRUE
print("Result of",a,"> 2 and",a,"< 10 is",result)

a = 1
result = a > 2 and a < 10   # F
print("Result of", a,"> 2 and", a,"< 10 is", result)

# Logical or opertor
a=5                                         #TRUE
result= a > 2 or a < 10 
print("Result of",a,"> 2 or",a,"< 10 is",result)

a=11                                    #FALSE
result= a > 2 or a < 10
print("Result of",a,"> 2 or",a,"< 10 is",result)

#logical not operator
a=5                                       #false
result= not(a > 2 and a < 10)
print("Result of not(",a,"> 2 and",a,"< 10) is",result)

a=15                                      #true
result= not(a > 2 and a < 10)   
print("Result of not(",a,"> 2 and",a,"< 10) is",result)
