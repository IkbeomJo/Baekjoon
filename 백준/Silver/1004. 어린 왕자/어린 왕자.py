T = int(input())
for _ in range(T):
    count = 0
    x1,y1,x2,y2 = map(int, input().split())
    N = int(input())
    for _ in range(N):
        px,py,pr = map(int, input().split())
        
        if (x1 - px)**2 + (y1 - py)**2 < pr**2 and (x2 - px)**2 + (y2 - py)**2 < pr**2:
            continue
        elif (x1 - px)**2 + (y1 - py)**2 < pr**2 or (x2 - px)**2 + (y2 - py)**2 < pr**2:
            count += 1
            
    print(count)
    