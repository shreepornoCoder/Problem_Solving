T = int(input())

num = list(map(int, input().split()))
min_num = min(num)

min_num_cnt = num.count(min_num)

if min_num_cnt % 2 != 0:
    print("Lucky")

else:
    print("Unlucky")