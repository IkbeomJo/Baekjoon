N = int(input())

def hansu(n):
    count = 0
    for i in range(1, n+1):
        a = str(i)
        if(i<100):
            count+=1
        elif(int(a[0])-int(a[1]) == int(a[1])-int(a[2])):
            count+=1
    return count
    
print(hansu(N))