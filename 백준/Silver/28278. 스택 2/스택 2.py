import sys
N = int(input())
stack = list()
for i in range(N):
    x = list(map(int, sys.stdin.readline().split(' ')))
    if x[0] == 1:
        stack.append(x[1])
    elif (x[0] == 2 and len(stack)==0 ) or (x[0] == 5 and len(stack) == 0):
        print(-1)
    elif x[0] == 2:
        print(stack.pop())
    elif x[0] == 3:
        print(len(stack))
    elif x[0] == 4:
        print(0) if len(stack) else print(1)
    elif x[0] == 5:
        print(stack[-1])