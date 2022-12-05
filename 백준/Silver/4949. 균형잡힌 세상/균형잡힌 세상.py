import sys

bracket = ['[', ']', '(', ')']
while True:
    S = sys.stdin.readline()
    if S == '.\n':break
    Stack = list()
    for i in range(len(S)):
        if S[i] in bracket:
            if S[i] == bracket[0] or S[i] == bracket[2]:
                Stack.append(S[i])

            elif len(Stack) == 0 or Stack[-1] != bracket[bracket.index(S[i])-1]:
                print('no')
                break
            else:
                Stack.pop()
        if i == len(S) - 1 and len(Stack) == 0:
            print('yes')
        elif i == len(S) - 1 and len(Stack) != 0:
            print('no')