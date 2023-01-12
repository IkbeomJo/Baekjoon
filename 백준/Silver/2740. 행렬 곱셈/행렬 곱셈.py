N, M = map(int, input().split())
A = list()
B = list()
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())

for _ in range(M):
    B.append(list(map(int, input().split())))

result = [[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        empty = 0
        for z in range(M):
            empty += A[i][z] * B[z][j]
        result[i][j] = empty

for i in range(N):
    for j in range(K):
        print(result[i][j],end=' ')
    print('')
