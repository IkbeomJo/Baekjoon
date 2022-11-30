import sys

N = int(input())
stack = list()
for _ in range(N):
    Command = sys.stdin.readline().split()

    if Command[0] == 'push':
        stack.append(int(Command[1]))
    elif Command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(len(stack)-1))
    elif Command[0] == 'size':
        print(len(stack))
    elif Command[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif Command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])