import sys
T = int(input())

for _ in range(T):
    L = list(map(int,sys.stdin.readline().split(" ")))
    L.sort()
    a= L[0]
    b= L[1]
    while True:
        x = a % b
        a = b
        b = x
        
        if x==0:
            break
        
    b = L[0]*L[1]//a
    print(b)