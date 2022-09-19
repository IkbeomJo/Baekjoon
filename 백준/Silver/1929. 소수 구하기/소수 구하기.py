M,N = map(int, input().split())
L = list()

for i in range(M, N+1):
    check = True
    if i == 1:
        continue
        
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            check = False
            break
            
    if check:
        L.append(i)
        
for i in L:
    print(i)