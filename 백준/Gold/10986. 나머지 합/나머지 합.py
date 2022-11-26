N, M = map(int, input().split())
A = list(map(int, input().split()))

sum_prefix = [A[0]]
count_num = [0 for _ in range(M)]
for i in range(1,N):
    sum_prefix.append(sum_prefix[i-1]+A[i])

for i in range(N):
    sum_prefix[i] %= M
    count_num[sum_prefix[i]] += 1

cnt_result = sum_prefix.count(0)

for i in count_num:
    if i > 1:
        x = i * (i-1) // 2
        cnt_result += x

print(cnt_result)