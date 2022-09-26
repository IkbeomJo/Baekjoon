import math
T = int(input())
for _ in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int,input().split(" "))
    
    d = math.sqrt((x_2 - x_1)**2 + (y_2-y_1)**2)
    if d == 0 and r_1 == r_2:
        print("-1")
    
    elif abs(r_1 - r_2) == d or r_1 + r_2 == d:
        print("1")
    
    elif abs(r_1 - r_2) < d < r_1+r_2:
        print("2")
        
    else:
        print("0")
        
    
    