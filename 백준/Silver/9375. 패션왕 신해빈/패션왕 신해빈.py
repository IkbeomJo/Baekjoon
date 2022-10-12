T = int(input())

for _ in range(T):
    n = int(input())
    L_s = list()
    L = list()
    result = 1
    
    for _ in range(n):
        S1, S2 = input().split()
        L.append(S2)
        if S2 in L_s:
            continue
        else:
            L_s.append(S2)
    
    
    for i in L_s:
        result *= L.count(i)+1
        
    

    print(result-1)