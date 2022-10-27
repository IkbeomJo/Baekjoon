N, M = map(int, input().split())
L = list()
L2 = list()
for i in range(N):
    L.append(list(map(int, input().split())))

for i in range(N):
    L2.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        print(L[i][j]+L2[i][j],end=" ")
    print()