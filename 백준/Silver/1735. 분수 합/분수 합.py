def gcd(n, m):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if n % m == 0:
        return n
    else:
        return gcd(n, m%n)

A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
S1 = A1*B2 + A2*B1
S2 = A2 * B2
x = gcd(S2, S1)

print(S1//x, S2//x)