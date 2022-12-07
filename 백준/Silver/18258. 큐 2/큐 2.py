import sys
from collections import deque
N = int(input())
queue = deque()
for _ in range(N):
    Command = sys.stdin.readline().split()

    if Command[0] == 'push':
        queue.append(int(Command[1]))

    elif Command[0] == 'pop':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)

    elif Command[0] == 'size':
        print(len(queue))

    elif Command[0] == 'empty':
        print(1 if len(queue) == 0 else 0)

    elif Command[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif Command[0] == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)