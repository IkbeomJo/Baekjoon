import sys
def gcd(n, m):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if n % m == 0:
        return n
    else:
        return gcd(n, m%n)

T = int(input())
first_value = int(input())
empty_value = int(input())
colonnade_between = [empty_value-first_value]
gcd_value = 1000000000
cnt = 0

for _ in range(T-2):
    x = int(sys.stdin.readline())
    colonnade_between.append(x - empty_value)
    empty_value = x

for i in range(1, T-1):
    x = gcd(colonnade_between[i],colonnade_between[i-1])
    if x < gcd_value: gcd_value = x


for i in range(first_value, first_value+sum(colonnade_between)+1,gcd_value):
    cnt+=1

print(cnt-T)