def queen(N):
    global cnt
    cnt = 0
    L = [None for _ in range(N)]
    visited = [False for _ in range(N)]
    n = 0
    
    def back(n):
        if n == N:
            global cnt
            cnt += 1
            return
        
        for i in range(N):
            if visited[i]:
                continue
                
            L[n] = i
            
            if checkqueen(n):
                visited[i] = True
                back(n+1)
                visited[i] = False
    
    def checkqueen(n):
        for i in range(n):
            if L[n] == L[i] or abs(n-i) == abs(L[i] - L[n]):
                return False
        
        return True
    
    back(n)
    return cnt

N = int(input())

print(queen(N))