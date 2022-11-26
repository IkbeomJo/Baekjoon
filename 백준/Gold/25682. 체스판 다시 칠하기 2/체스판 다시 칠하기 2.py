import sys
N, M, K = map(int, sys.stdin.readline().split())
BW_table = list()
W_prefix_table = [[0 for _ in range(M+1)] for _ in range(N+1)]
B_prefix_table = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N):
    BW_table.append(input())

for i in range(N):
    for j in range(M):
        if (i+j) % 2 == 0:
            if BW_table[i][j] == 'B':
                B_prefix_table[i+1][j+1] = B_prefix_table[i+1][j]
                W_prefix_table[i+1][j+1] += W_prefix_table[i+1][j]+1
            else:
                W_prefix_table[i + 1][j + 1] = W_prefix_table[i + 1][j]
                B_prefix_table[i + 1][j + 1] += B_prefix_table[i + 1][j]+1
        else:
            if BW_table[i][j] == 'B':
                W_prefix_table[i + 1][j + 1] = W_prefix_table[i + 1][j]
                B_prefix_table[i + 1][j + 1] += B_prefix_table[i + 1][j] + 1
            else:
                B_prefix_table[i + 1][j + 1] = B_prefix_table[i + 1][j]
                W_prefix_table[i + 1][j + 1] += W_prefix_table[i + 1][j] + 1

for i in range(2,N+1):
    for j in range(1,M+1):
        B_prefix_table[i][j] += B_prefix_table[i-1][j]
        W_prefix_table[i][j] += W_prefix_table[i-1][j]

min_result = 10000000000
for i in range(K, N+1):
    for j in range(K, M+1):
        B_min = B_prefix_table[i][j] - B_prefix_table[i-K][j] - B_prefix_table[i][j-K] + B_prefix_table[i-K][j-K]
        W_min = W_prefix_table[i][j] - W_prefix_table[i-K][j] - W_prefix_table[i][j-K] + W_prefix_table[i-K][j-K]

        if min(B_min, W_min) < min_result:
            min_result = min(B_min, W_min)

print(min_result)
