# print("HEY")
import numpy as np

## Python List Example
# x = [10,20,30,40,50]
# y = [100,200,300,400,500]

# print(x+y)

## Numpy array Example

# arr_x = np.array(x)
# arr_y = np.array(y)
# print(arr_x+arr_y)
value = 10

list1 = list(range(value))
list2 = list(range(value))
list3 = []

for i in range(value):
    x = list1[i] + list2[i]
    list3.append(x)

print(list3)
    




