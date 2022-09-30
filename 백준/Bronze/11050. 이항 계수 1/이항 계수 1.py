def fac(n):
    ans = 1
    for i in range(2, n+1):
        ans = ans * i
    return ans

N, K = map(int, input().split(" "))

n_f = fac(N)
k_f = fac(K)
nk_f = fac(N-K)

print(int(n_f/(k_f*nk_f)))