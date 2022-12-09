import sys
from collections import deque

N, K = map(int, input().split())
Josephus = deque(i for i in range(1,N+1))
result = list()

while Josephus:
    for i in range(K-1):
        Josephus.append(Josephus.popleft())

    result.append(Josephus.popleft())


print("<",end='')
for i in range(len(result)-1):
    print(f"{result[i]},",end=' ')
print(result[N-1],end='')
print(">")
