n = int(input())
L = list()
for i in range(1,n+1):
    L.append(n//i*i)

print(sum(L))