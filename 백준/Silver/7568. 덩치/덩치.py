N = int(input())
L= list()
for i in range(N):
    L.append(list(map(int,input().split())))
    
for i in range(N):
    rank=N
    for j in range(N):
        if i == j:
            continue
            
        elif L[i][0]>=L[j][0]:
            rank-=1
        elif L[i][1]>=L[j][1]:
            rank-=1
    print(rank)
