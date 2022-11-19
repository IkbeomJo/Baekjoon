n = int(input())

L = list()
for i in range(n):
    L.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            L[i][j] = L[i][j] + L[i-1][j]
        elif j == i:
            L[i][j] = L[i][j] + L[i-1][j-1]
        else:
            L[i][j] = L[i][j] + max(L[i-1][j], L[i-1][j-1])

print(max(L[n-1]))