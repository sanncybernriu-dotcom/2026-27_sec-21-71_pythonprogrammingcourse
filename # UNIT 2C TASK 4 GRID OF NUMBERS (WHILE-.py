# UNIT 2C TASK 4  GRID OF NUMBERS (WHILE-FOR)#
num = 1
row_loop_var = 1
while row_loop_var <= 3:
    for column_loop_var in range(1, 4):
        print(num, end=" ")
        num = num + 1
    print()
    row_loop_var = row_loop_var + 1