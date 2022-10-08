N = int(input())
L = list(map(int, input().split()))
def Euclidean(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

for i in range(1,len(L)):
    if L[0] % L[i] == 0:
        print(f"{L[0] // L[i]}/1")
    else:
        x = Euclidean(L[0],L[i])
        print(f"{L[0]//x}/{L[i]//x}")
        