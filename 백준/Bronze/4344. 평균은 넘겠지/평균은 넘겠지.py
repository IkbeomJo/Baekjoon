N = int(input())
count=0
per = 0
avg = 0
sum_v=0
for i in range(N):
    x = list(map(int,input().split()))
    
    for j in range(1,len(x)):
        sum_v += x[j]
    avg = sum_v/x[0]
    for j in range(1, len(x)):
        if(x[j]>avg):
            count+=1
    per = format(count/x[0] * 100, ".3f") + "%"
    print(per)
    sum_v = 0
    avg = 0
    count = 0
    per = 0