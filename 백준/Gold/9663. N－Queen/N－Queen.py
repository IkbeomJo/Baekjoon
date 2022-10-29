def back(n):
    if n == N:
        global cnt
        cnt += 1
        return
    
    for i in range(N):
        L[n] = i
        if checkqueen(n):
            back(n+1)
    
def checkqueen(n):
    for i in range(n):
        if L[n] == L[i] or n-i == abs(L[i] - L[n]):
            return False
        
    return True
    
N = int(input())
L = [0 for _ in range(N)]
global cnt
cnt = 0
back(0)
print(cnt)