def back(L):
    for i in range(1,N+1):
        if len(L) == M:
            print(*L)
            
            return
        
        
        L.append(i)
        back(L)
        L.pop()
        
    

N, M = map(int,input().split())
L = list()
back(L)