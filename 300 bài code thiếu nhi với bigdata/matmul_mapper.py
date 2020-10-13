#!/usr/bin/python3
## Mapper cho phép nhân ma trận Z = X*Y

import sys

# biết trước row và col 
Z_ROW = 2
Z_COL = 2

# Input có thể là 1 file rất to, chứa các data của X, Y
for line in sys.stdin:
    
    # Data mỗi dòng cần theo format này: "tên matrix, số row, số col, value". VD: "X,1,1,7" là dòng 1 cột 1 của X = 7
    # các dòng không cần theo thứ tự row, col của X hoặc Y
    matrix, row, col, value = line.strip().split(',')

    if (matrix == 'X'):
        # Nếu là matrix X thì sẽ thực hiện Z_COL phép nhân
        for c in range(1, Z_COL + 1):
            mapper_key = 'Z({0},{1})'.format(row, c)
            mapper_val = '{0},{1},{2}'.format(col, matrix, value)
            print('{0}\t{1}'.format(mapper_key, mapper_val))
    else:
        # Tương tự logic với matrix Y
        for r in range(1, Z_ROW + 1):
            mapper_key = 'Z({0},{1})'.format(r, col)
            mapper_val = '{0},{1},{2}'.format(row, matrix, value)
            print('{0}\t{1}'.format(mapper_key, mapper_val))

