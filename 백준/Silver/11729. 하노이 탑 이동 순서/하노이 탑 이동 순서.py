N = int(input())
count=0
L=list()
def hanoi(num,a,c,b):
    global count, L
    count+=1
    if num == 1:
        L.append([a,c])
        return
    
    hanoi(num-1,a,b,c)
    L.append([a,c])
    hanoi(num-1,b,c,a)
    
hanoi(N,1,3,2)

print(count)
for i in L:
    print(i[0],i[1])