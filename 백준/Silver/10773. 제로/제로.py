import sys
K = int(sys.stdin.readline())
Stack = list()

for _ in range(K):
    command_int = int(sys.stdin.readline())
    if command_int == 0 :
        Stack.pop(-1)
    else:
        Stack.append(command_int)

print(sum(Stack))