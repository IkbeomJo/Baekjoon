N = int(input())
L = list()
re_L = list()

def Euclidean(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

for _ in range(N):
    L.append(int(input()))
    
L.sort()    
for i in range(1,N):
    re_L.append(L[i]-L[i-1])

GCD = 0
for i in re_L:
    if GCD == 0:
        GCD = i
        continue
    GCD = Euclidean(GCD,i)

result = set()
for i in range(2,int(GCD**0.5)+1):
    if GCD % i == 0:
        result.add(i)
        result.add(GCD//i)
result.add(GCD)
result = sorted(list(result))
print(*result)
