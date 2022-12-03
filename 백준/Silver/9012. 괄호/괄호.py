import sys
T = int(sys.stdin.readline())
Stack = list()

for _ in range(T):
    PS = sys.stdin.readline()
    Stack = list()
    for i in range(len(PS)):
        if PS[i] == '(':
            Stack.append(1)

        elif PS[i] == ')':
            if len(Stack) == 0:
                Stack.append(1)
                break
            else:
                Stack.pop(-1)

    if len(Stack) == 0:
        print('YES')
    else:
        print('NO')

