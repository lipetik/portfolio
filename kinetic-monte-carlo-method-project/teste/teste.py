import numpy as np
from numpy import column_stack, savetxt

arr_x = [1, 2, 3, 4]
arr_y = [1, 4, 9, 16]

data = column_stack([arr_x, arr_y])
label = ['x', 'y']
label_row = ','.join(label)
myheader = label_row
savetxt('text.csv', data, delimiter=',', header=myheader)



