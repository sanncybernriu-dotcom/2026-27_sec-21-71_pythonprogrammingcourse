# This program checks if a person is eligible to vote based on their age.

age_in_years =int(input("Enter your age in years:"))

if age_in_years >=18:                                    #if condition to check if the age is greater than or equal to 18
    print("You are eligible to vote.")

else:                                                     #else condition to check if the age is less than 18
    print("You are not eligible to vote.")