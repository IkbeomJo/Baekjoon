import sys
from collections import deque

N = int(input())
queue = deque()
for _ in range(N):
    Command = sys.stdin.readline().split()

    if Command[0] == "push_front":
        queue.appendleft(Command[1])

    elif Command[0] == "push_back":
        queue.append(Command[1])

    elif Command[0] == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif Command[0] == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())

    elif Command[0] == "size":
        print(len(queue))

    elif Command[0] == "empty":
        print(1 if len(queue) == 0 else 0)

    elif Command[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            
    elif Command[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])