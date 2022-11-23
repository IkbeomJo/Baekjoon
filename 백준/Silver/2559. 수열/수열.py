import sys
N, K = map(int,input().split())

L = list(map(int,input().split()))
sum_diff = [sum(L[0:K])]
for i in range(N-K):
    sum_diff.append(sum_diff[i] + L[i+K] - L[i])

print(max(sum_diff))

