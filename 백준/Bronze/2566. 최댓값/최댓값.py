L = list()
max = -1
max_index = list()

for i in range(9):
    L.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if L[i][j] > max:
            max = L[i][j]
            max_index = [i,j]

print(max)
print(max_index[0]+1,max_index[1]+1)