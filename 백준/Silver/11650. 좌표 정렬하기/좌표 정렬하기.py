import sys
N = int(input())
L = list()

for i in range(N):
    [x, y] = map(int,sys.stdin.readline().split(" "))
    L.append([x, y])

L.sort()
for i in range(N):
    print(L[i][0],L[i][1])