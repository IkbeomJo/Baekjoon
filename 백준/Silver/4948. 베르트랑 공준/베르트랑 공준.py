def check(num):
    for j in range(2,int(num**0.5)+1):
        if i%j == 0:
            return False
    return True
        
L = list()
for i in range(2,246912):
    if check(i):
        L.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    count = 0    
    for i in L:
        if n<i<=2*n:
            count+=1
            
    print(count)  