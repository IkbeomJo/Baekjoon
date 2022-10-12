def fec(N):
    result = 1
    for i in range(1,N+1):
        result *= i
        
    return result

N = int(input())
x = str(fec(N))
cnt = 0
for i in range(1,len(x)):
    if x[-i] == "0":
        cnt+=1
    else:
        break

print(cnt)