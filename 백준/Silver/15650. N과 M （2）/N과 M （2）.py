def back(L,n):
    for i in range(n,N+1):
        if len(L) == M:
            print(*L)
            
            return
        
        elif i not in L:
            L.append(i)
            back(L,i)
            L.pop()
        
    

N, M = map(int,input().split())
L = list()
n=1
back(L,n)