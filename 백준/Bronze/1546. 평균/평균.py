N = int(input())
exam = list(map(int, input().split()))
M=exam[0]
sum_v = 0
for i in range(N):
    if(exam[i]>M):
        M=exam[i]

for i in range(N):
    exam[i] = (exam[i] / M) * 100
    sum_v += exam[i]
    

print(sum_v/N)