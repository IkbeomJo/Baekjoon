n = int(input())
dp = [0 for i in range(301)]
L = [0 for i in range(301)]
for i in range(n):
    L[i] = int(input())


dp[0] = L[0]
if n > 1:
    dp[1] = L[0]+L[1]
    if n > 2:
        dp[2] = max(L[0]+L[2],L[1]+L[2])
        for i in range(3, n):
            dp[i] = max(dp[i-3]+L[i-1]+L[i],dp[i-2]+L[i])
print(dp[n-1])
