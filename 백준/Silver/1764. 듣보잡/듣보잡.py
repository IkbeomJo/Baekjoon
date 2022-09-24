import sys
N, M = map(int,input().split(" "))
S_1 = set()
S_2 = list()
result = list()

for i in range(N):
    S_1.add(sys.stdin.readline().strip())
    
for i in range(M):
    S_2.append(sys.stdin.readline().strip())
    
for i in S_2:
    if i in S_1:
        result.append(i)

print(len(result))
result.sort()
for i in result:
    print(i)