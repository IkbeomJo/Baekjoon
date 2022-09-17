N = int(input())
L = [0]*50

for i in range(N):
    x = input()
    if L[len(x)-1] == 0:
        L[len(x)-1] = [x]
    else:
        if x not in L[len(x)-1]:
            L[len(x)-1].append(x)

for i in range(50):
    if L[i] != 0:
        V = sorted(L[i])
        for j in V:
            print(j)