values_list = list(map(int, input().split()))

total_contestant = values_list[0]
k_value = values_list[1]

values_list = list(map(int, input().split()))
ans = 0

for point in values_list:
    if point >= values_list[k_value-1] and point != 0:
        ans+=1

print(ans)