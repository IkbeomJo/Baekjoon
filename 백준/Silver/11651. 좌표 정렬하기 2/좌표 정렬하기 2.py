import sys
N = int(input())
L = list()

for i in range(N):
    [x, y] = map(int,sys.stdin.readline().split(" "))
    L.append([y, x])

L.sort()
for i in range(N):
    print(L[i][1],L[i][0])