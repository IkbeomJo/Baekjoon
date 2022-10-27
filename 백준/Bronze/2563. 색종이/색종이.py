L = list()

L= [[0 for i in range(100)]for i in range(100)]



N = int(input())

for i in range(N):
    x,y = map(int, input().split())
    for i in range(x-1,x+9):
        for j in range(y-1,y+9):
            L[i][j] += 1


count = 0

for i in range(100):
    for j in range(100):
        if L[i][j] >= 1:
            count += 1

print(count)