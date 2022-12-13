import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
spin_queue = deque(i for i in range(1,N+1))
find_result = list(map(int, sys.stdin.readline().split()))
cnt = 0

for x in find_result:
    if spin_queue.index(x) == 0:
        spin_queue.popleft()

    elif spin_queue.index(x) <= len(spin_queue) // 2:
        while spin_queue[0] != x:
            spin_queue.append(spin_queue.popleft())
            cnt += 1
        spin_queue.popleft()

    else:
        while spin_queue[0] != x:
            spin_queue.appendleft(spin_queue.pop())
            cnt += 1
        spin_queue.popleft()

print(cnt)

