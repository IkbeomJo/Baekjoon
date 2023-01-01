n, k = map(int, input().split())
bag = [[0,0]]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(n):
    bag.append(list(map(int, input().split())))

bag.sort()

for i in range(1,n+1):
    for j in range(1,k+1):
        value = bag[i][1]
        weight = bag[i][0]
        if weight > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])

print(max(max(dp)))
