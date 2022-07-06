T = int(input())

num = 1

for i in range(T):
    L = list()
    k = int(input())
    n = int(input())
    for i in range(1,n+1):
        L.append(i)
    for i in range(k):
        sum_v = 0
        for i in range(n):
            sum_v += L[i]
            L[i] = sum_v
    print(L[n-1])
        