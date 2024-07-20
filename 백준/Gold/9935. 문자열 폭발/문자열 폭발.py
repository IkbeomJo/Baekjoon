new_str = list(input())
bomb = input()
stack = list()

for i in range(len(new_str)):
    stack.append(new_str[i])
    if ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    for i in stack:
        print(i,end='')

