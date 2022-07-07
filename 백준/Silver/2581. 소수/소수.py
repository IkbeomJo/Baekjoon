M= int(input())
N= int(input())
sum_v = 0
L = list()
for i in range(M, N+1):
    check = True
    if i == 1:
        continue
        
    for j in range(2,i):
        if i%j == 0:
            check = False
            break
            
    if check:
        L.append(i)
        sum_v += i

if sum_v == 0 :
    sum_v = -1
    print(sum_v)
else:
    print(sum_v)
    print(L[0])
