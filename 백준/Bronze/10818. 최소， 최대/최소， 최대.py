N= int(input())
A= list(map(int, input().split()))
max_v = A[0] 
min_v = A[0]
for i in range(N):
    if(A[i]<min_v):
        min_v = A[i]
    elif(A[i]>max_v):
        max_v = A[i]

print(min_v, max_v)