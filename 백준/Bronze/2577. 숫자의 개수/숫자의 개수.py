A = int(input())
B = int(input())
C = int(input())
result = str(A*B*C)
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
N = None
for i in range(len(result)):
    N = int(result[i])
    count[N]+=1
    
for i in range(10):
    print(count[i])