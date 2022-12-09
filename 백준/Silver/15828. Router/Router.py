import sys
from collections import deque

N = int(input())
router = deque()

while True:
    packet = int(sys.stdin.readline())
    if packet == -1:
        break
    elif packet and len(router) < N:
        router.append(packet)

    elif not packet:
        router.popleft()

if len(router):
    print(*router)
else:
    print("empty")