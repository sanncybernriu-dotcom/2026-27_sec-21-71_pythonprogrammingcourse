#Finding grades using if elif ladder
marks=int(input("Enter a number:"))
if marks<70:
    print(f"Grade:D (marks = {marks})")
elif marks >= 70 and marks < 80:
    print(f"Grade:C (marks = {marks})")
elif marks >= 80 and marks < 90:
    print(f"Grade:B (marks = {marks})")
else:
    print(f"Grade:A (marks = {marks})")