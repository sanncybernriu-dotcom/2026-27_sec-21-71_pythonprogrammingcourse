# UNIT-3D-TASK 6 PRINT DETAILS WITH **KWARGS
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name="Krishna", age=26, city="Guntur")