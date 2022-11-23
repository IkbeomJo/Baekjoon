import sys
N, M = map(int,input().split())

L = list(map(int,input().split()))
for i in range(1,N):
    L[i] += L[i-1]

for _ in range(M):
    i, j = map(int,sys.stdin.readline().split())
    if i == 1:
        print(L[j-1])

    else:
        print(L[j-1]-L[i-2])

