X = int(input())
N = 1
C = 2

while True:
    if(X<=N):
        break
    N += C
    C += 1
    
if C%2 == 1:
    print(f"{C-((N+1)-X)}/{(N+1)-X}")
else:
    print(f"{(N+1)-X}/{C-((N+1)-X)}")