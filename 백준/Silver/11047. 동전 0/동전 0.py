import sys
N, K = map(int, input().split())

coin_cnt = 0
coin_value_list = list()
for _ in range(N):
    coin_value_list.append(int(input()))

for i in range(N-1,-1,-1):
    if K >= coin_value_list[i]:
        x = K // coin_value_list[i]
        K -= coin_value_list[i] * x
        coin_cnt += x

print(coin_cnt)