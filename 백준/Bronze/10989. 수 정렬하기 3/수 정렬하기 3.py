import sys 
N = int(input())
L = [0]*10000

for i in range(N):
    L[int(sys.stdin.readline())-1]+=1
    
for i in range(10000):
    if L[i] != 0:
        for j in range(L[i]):
            print(i+1)