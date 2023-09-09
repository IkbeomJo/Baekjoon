N = int(input())
schedule = [[0,0]]
dp = [0 for i in range(N+1000)]
for _ in range(N):
    schedule.append(list(map(int, input().split())))

result = 0
for day in range(N, 0, -1):
    if schedule[day][0] + day > N + 1:
        dp[day] = dp[day+1]

    else:
        dp[day] = max(dp[schedule[day][0] + day] + schedule[day][1],dp[day+1])

print(max(dp))