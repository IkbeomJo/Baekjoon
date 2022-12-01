N = int(input())
A = list(map(int, input().split()))
increase = [1 for _ in range(N)]
decrease = [1 for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if A[i] < A[j]:
            increase[j] = max(increase[j],increase[i]+1)

for i in range(N-1,-1,-1):
    for j in range(i-1,-1,-1):
        if A[i] < A[j]:
            decrease[j] = max(decrease[j], decrease[i]+1)

dp = [increase[i] + decrease[i] for i in range(N)]

print(max(dp)-1)


