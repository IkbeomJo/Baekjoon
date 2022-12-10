import sys
from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    printer = deque(i for i in range(N))
    printer_importance = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    while M in printer:
        if printer_importance[0] == max(printer_importance):
            printer_importance.popleft()
            printer.popleft()
            cnt += 1
        else:
            printer_importance.append(printer_importance.popleft())
            printer.append(printer.popleft())
    print(cnt)