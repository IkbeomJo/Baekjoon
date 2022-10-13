def back(L,n):
    for i in range(n,N+1):
        if len(L) == M:
            print(*L)
            
            return
        
        
        L.append(i)
        back(L, i)
        L.pop()
        
    
n = 1
N, M = map(int,input().split())
L = list()
back(L,n)