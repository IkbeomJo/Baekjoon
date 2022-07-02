num = list()
count = 0
check = False

for i in range(10):
    num.append(int(input())%42)

for i in range(10):
    for j in range(i+1,10):
        if(num[i] == num[j]):
            check = True
    
    if(check == True):
        check = False
    else:
        count+=1

print(count)