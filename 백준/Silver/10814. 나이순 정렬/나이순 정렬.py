import sys
N = int(input())
L = [0]*200

for i in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    
    if L[age-1] == 0:
        L[age-1] = [name]
    else:
        L[age-1].append(name)
    
for i in range(200):
    if L[i] != 0 :
        for j in range(len(L[i])):
            print(i+1, L[i][j])
