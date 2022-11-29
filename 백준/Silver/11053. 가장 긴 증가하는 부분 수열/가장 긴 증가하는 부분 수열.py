N = int(input())
A = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i+1,N):
        if A[i] < A[j]:
            dp[j] = max(dp[j],dp[i] + 1)

print(max(dp))