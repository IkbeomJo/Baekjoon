def fec(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

n, k = map(int, input().split())

nk = fec(n)//(fec(k)*fec(n-k))

print(nk%10007)
    