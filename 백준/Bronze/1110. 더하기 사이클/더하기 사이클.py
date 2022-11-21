N = int(input())
count = 0
num=0
temp=0
if(N<10):
    num = N*10
    N = N*10
else:
    num = N

while(1):
    temp=int(num/10) + (num%10)
    num=(num%10)*10 + (temp%10)
    count+=1
    if(num==N):
        break
print(count)