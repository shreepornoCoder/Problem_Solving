from math import *

size_of_arr = int(input())

children = list(map(int, input().split()))

cnt = 0
res = 0
for i in range(0, size_of_arr):
    if children[i] == 4: 
        cnt+=1
    else:
        res += children[i]

print(cnt + (res // 4))