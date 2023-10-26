H, W, X, Y = map(int,input().split())
B = []
for i in range(H+X):
    B.append(list(map(int,input().split())))

A = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if (i < H and j < W) and (i >= X and j >= Y):
            A[i][j] = B[i][j] - A[i-X][j-Y]
        elif i < H and j < W:
            A[i][j] = B[i][j]
        else:
            A[i][j] = 0

for i in range(H):
    for j in range(W):
        print(A[i][j],end=' ')
    print()