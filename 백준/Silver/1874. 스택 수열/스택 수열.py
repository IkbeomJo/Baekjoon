import sys

n = int(input())
Stack = [1]
arr = list()
PushPop_result = ['+']
cnt = 2
for _ in range(n):
    arr.append(int(sys.stdin.readline()))


for i in range(n):
    if len(Stack) == 0:
        Stack.append(cnt)
        cnt += 1
        PushPop_result.append('+')

    while Stack[-1] < arr[i] or len(Stack) == 0:
        Stack.append(cnt)
        cnt += 1
        PushPop_result.append('+')

    if Stack[-1] == arr[i]:
        PushPop_result.append('-')
        Stack.pop()
    else:
        print('NO')
        exit(0)

for i in PushPop_result: print(i)