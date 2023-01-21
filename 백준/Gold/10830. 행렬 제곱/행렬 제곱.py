N, B = map(int, input().split())
A = list()
for i in range(N):
    A.append(list(map(int, input().split())))

def matrix_mul(U, V):
    n = len(U)
    res = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            res[row][col] = e % 1000

    return res

def matrix_multiple(A, B):
    if B >= 2:
        x = matrix_multiple(A, B // 2)
        if B % 2:
            return matrix_mul(matrix_mul(x,x),A)
        else:
            return matrix_mul(x,x)
    else:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A

result = matrix_multiple(A, B)

for i in range(N):
    print(*result[i])