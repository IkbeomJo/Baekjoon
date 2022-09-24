N = int(input())
S = list(map(int,input().split(" ")))
D = {0 : 0}

M = int(input())
L = list(map(int, input().split(" ")))

for i in S:
    if i in D:
        D[i] = D[i]+1
    else:
        D[i] = 1
    
for i in L:
    if (i in D):
        print(D[i],end=" ")
    else:
        print("0", end=" ")