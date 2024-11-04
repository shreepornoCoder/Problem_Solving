import sys

# function for taking input
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

# functions for solving the problem
def find_max_min(length, arr):
    max_num = 0
    min_num = 1e5

    for i in range(length):
        if arr[i]>max_num:
            max_num = arr[i]
        else:
            if arr[i]<min_num:
                min_num = arr[i]

    print(min_num, max_num)

a = int(input())
arr = get_ints()

find_max_min(a, arr)