import heapq
import sys
A = list()
N = int(input())

for i in range(N):
    x = -int(sys.stdin.readline())
    if x == 0 and len(A) == 0:
        print("0")
    elif x == 0:
        print(-heapq.heappop(A))

    else:
        heapq.heappush(A,x)



