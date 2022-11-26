import sys
N, M = map(int, sys.stdin.readline().split())
table_L = [[0 for i in range(N+1)]]

for i in range(1,N+1):
    table_L.append(list(map(int, sys.stdin.readline().split())))
    table_L[i].insert(0, 0)

    for j in range(1, N+1):
        table_L[i][j] += table_L[i][j-1]

    for j in range(1, N+1):
        table_L[i][j] += table_L[i-1][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(table_L[x2][y2] - table_L[x2][y1-1] - table_L[x1-1][y2] + table_L[x1-1][y1-1])