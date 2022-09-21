M, N = map(int, input().split(" "))
L = list()
for i in range(M):
    L.append(input())
min_L = list()
count = 0
for i in range(M-7):
    for j in range(N-7):
        first_W = 0
        first_B = 0
        for x in range(i,i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if L[x][y] == "B":
                        first_W +=1
                    else:
                        first_B +=1
                else:
                    if L[x][y] == "B":
                        first_B += 1
                    else:
                        first_W += 1
        
        min_L.append(first_B)
        min_L.append(first_W)
                        

print(min(min_L))