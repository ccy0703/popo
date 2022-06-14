n,m = map(int,input("輸入 N 及 M 為:").split())
array_list = []

for i in range(n):
    nums = input(f"輸入矩陣數值第 {i+1} 列為:").split()
    array_list.append(nums)

import numpy as np
outside = np.array(array_list).T
x = 1
print()

for i in outside:
    print(f"輸出矩陣數值第 {x} 列為:",end="")
    for j in i:
        print(j,end=" ")
    print()
    x += 1