import heapq
import sys

int_heap = list()
neg_heap = list()
N = int(input())

for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0 and len(int_heap)+len(neg_heap) == 0:
        print("0")
    elif x == 0 and len(int_heap) == 0:
        print(-heapq.heappop(neg_heap))
    elif x == 0 and len(neg_heap) == 0:
        print(heapq.heappop(int_heap))

    elif x == 0 and heapq.nsmallest(1,int_heap) >= heapq.nsmallest(1,neg_heap):
        print(-heapq.heappop(neg_heap))
    elif x == 0:
        print(heapq.heappop(int_heap))

    else:
        if x < 0:
            heapq.heappush(neg_heap,-x)
        else:
            heapq.heappush(int_heap,x)


