N, K = map(int, input().split())
P = 1000000007
def Fac(N):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % P
    return n

def div(A, B, C):
    if B == 0:
        return 1
    elif B == 1:
        return A

    x = div(A, B//2, C)
    if B % 2:
        return x * x * A % C
    else:
        return x * x % C

top = Fac(N)
bottom = Fac(N-K) * Fac(K)

print(top * div(bottom,P-2,P) % P)

#N!((N-K)! * K!)^^p-2 % P