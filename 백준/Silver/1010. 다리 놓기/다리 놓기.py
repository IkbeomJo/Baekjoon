def fec(N):
    result = 1
    for i in range(1,N+1):
        result *= i
        
    return result

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(fec(M)//(fec(N)*fec(M-N)))
