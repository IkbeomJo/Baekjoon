N = int(input())
OX = list()
count = 1
sum_v = 0

for i in range(N):
    OX.append(str(input()))
    for j in range(len(OX[i])):
        if(OX[i][j]=="O"):
            sum_v += count
            count += 1
        elif(OX[i][j]=="X"):
            count = 1
    print(sum_v)
    sum_v = 0
    count = 1