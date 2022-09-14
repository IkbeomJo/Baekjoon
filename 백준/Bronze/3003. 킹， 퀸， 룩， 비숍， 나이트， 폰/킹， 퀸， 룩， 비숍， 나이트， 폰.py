L= list(map(int,input().split()))
L_1 = [1,1,2,2,2,8]
L_2 = list()
for i in range(6):
    x = L_1[i]-L[i]
    print(x, end=" ")
