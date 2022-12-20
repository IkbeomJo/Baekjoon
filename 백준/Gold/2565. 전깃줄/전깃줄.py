N = int(input())
telephone_pole = [0 for _ in range(501)]
for i in range(N):
    A, B = map(int, input().split())
    telephone_pole[A] = B

for _ in range(501 - N):
    telephone_pole.remove(0)

dp = [1 for i in range(len(telephone_pole))]

for i in range(N):
    for j in range(i+1,N):
        if telephone_pole[i] < telephone_pole[j]:
            dp[j] = max(dp[i]+1, dp[j])

print(N-max(dp))