import sys
N = int(input())
L = list()
L_t = [0]*8001

for i in range(N):
    x = int(sys.stdin.readline())
    L.append(x)
    
    L_t[x+4000] += 1


L.sort()

one = round(sum(L) / N)

two = L[int((N-1)/2)] 

if L_t.count(max(L_t)) == 1:
    three = L_t.index(max(L_t))-4000
else:
    L_t[L_t.index(max(L_t))] = 0
    three = L_t.index(max(L_t))-4000



four = max(L)-min(L)

print(one)
print(two)
print(three)
print(four)
    