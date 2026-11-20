# UNIT-3D-TASK 8 STUDENT DETAILS WITH KWARGS
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
student_details(name="Anu", maths=85, science=90)