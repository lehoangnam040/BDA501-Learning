#!/usr/bin/python3
## Reducer cho phép nhân ma trận Z = X*Y

import sys

z_key = None 	# Key chứa thông tin hàng, cột của Z. VD z_key = Z(1,1)
z_cell = 0 	# giá trị của kết quả ở ô tương ứng với z_key 
first_val = None	# Giá trị đầu tiên trong phép nhân trong tích vô hướng hàng*cột 

for line in sys.stdin:
    key, val = line.strip().split('\t')
    index, _, value = val.split(',')
   
    if key == z_key:
        if first_val:
            # Nhân và cộng luôn vào kết quả tích vô hướng
            z_cell += first_val * float(value)
            first_val = None
        else:
            # Lưu lại cho phép nhân
            first_val = float(value)
    else:
        # Nếu đã tính đc bất kỳ ô nào của Z thì return
        if z_key:
            print('{0}\t{1}'.format(z_key, z_cell))
        # Reset 
        z_cell = 0
        first_val = float(value)
        z_key = key

# Ô cuối cùng
if key == z_key:
    print('{0}\t{1}'.format(z_key, z_cell))

