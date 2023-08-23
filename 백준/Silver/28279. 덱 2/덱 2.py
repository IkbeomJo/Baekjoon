import collections
import sys
deck = collections.deque([])

N = int(input())


for _ in range(N):
    cmd = list(map(int,sys.stdin.readline().split(' ')))

    if cmd[0] == 1:
        deck.appendleft(cmd[1])
    elif cmd[0] == 2:
        deck.append(cmd[1])
    elif cmd[0] == 3:
        if len(deck) == 0: print(-1)
        else: print(deck.popleft())
    elif cmd[0] == 4:
        if len(deck) == 0: print(-1)
        else: print(deck.pop())
    elif cmd[0] == 5:
        print(len(deck))
    elif cmd[0] == 6:
        if len(deck): print(0)
        else: print(1)
    elif cmd[0] == 7:
        if len(deck) == 0: print(-1)
        else: print(deck[0])
    elif cmd[0] == 8:
        if len(deck) == 0: print(-1)
        else: print(deck[-1])