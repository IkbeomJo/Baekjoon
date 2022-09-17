N = int(input())
L = list()
while N != 0:
    L.append(N%10)
    N = N//10

L.sort(reverse=True)
for i in L:
    print(i,end="")