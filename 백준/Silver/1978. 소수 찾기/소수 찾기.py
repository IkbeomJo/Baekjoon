N = int(input())
L = list(map(int,input().split()))

for i in range(N):
    if L[i]==1:
        N-=1
        continue

    for j in range(2,L[i]):
        if L[i]%j == 0:
            N-=1
            break

print(N)
        