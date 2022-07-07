def check(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

T = int(input())        
        
for i in range(T):
    n = int(input())
    d = n//2
    
    for j in range(d, 0, -1):
        if check(j) and check(n-j):
            print(j,n-j)
            break
