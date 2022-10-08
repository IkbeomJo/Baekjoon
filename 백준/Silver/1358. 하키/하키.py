w, h, x, y, p = map(int, input().split())
count = 0
for _ in range(p):
    px, py = map(int, input().split())
    r = h//2
    if px >= x and py >= y and px <= x+w and py <= y+h:
        count+=1
    elif (x-px)**2 + (y+r-py)**2 <= r**2 or (x+w-px)**2 + (y+r-py)**2 <= r**2:
        
        count+=1
print(count)