# This program checks if three given angles can form a valid triangle.

angle1_in_degrees = float(input("Enter the first angle in degrees: "))
angle2_in_degrees = float(input("Enter the second angle in degrees: "))
angle3_in_degrees = float(input("Enter the third angle in degrees: "))

if angle1_in_degrees > 0 and angle2_in_degrees > 0 and angle3_in_degrees > 0 and angle1_in_degrees + angle2_in_degrees + angle3_in_degrees == 180:
    print(f"The angles {angle1_in_degrees}, {angle2_in_degrees}, and {angle3_in_degrees} can form a triangle.")
else:
    print(f"The angles {angle1_in_degrees}, {angle2_in_degrees}, and {angle3_in_degrees} do not form a triangle.")
