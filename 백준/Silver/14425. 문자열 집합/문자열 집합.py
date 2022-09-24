N, M = map(int,input().split(" "))
S = set()
count = 0
for i in range(N):
    S.add(input())
    
for i in range(M):
    x = input()
    result = x in S
    if result == True:
        count +=1
    
print(count)