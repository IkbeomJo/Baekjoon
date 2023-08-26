import collections

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

cnt = 0
for x in range(N-1,-1,-1):
    if cnt == M: break
    if A[x] == 0:
        print(B[x],end=' ')
        cnt += 1

for i in range(M-cnt):
    print(C[i],end=' ')