N, M = map(int,input().split())
L= list(map(int,input().split()))
blackjac = 300000
result = None
check= None
for a in L:
    sun_v = 0
    for b in L:
        if a==b:
            continue
        for c in L:
            if c==b or c==a:
                continue
            if(a+b+c<=M):
                if(M-(a+b+c)<blackjac):
                    blackjac = M-(a+b+c)
                    result = a+b+c
            
print(result)    