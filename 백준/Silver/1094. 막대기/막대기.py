from collections import deque
X = int(input())
cnt = 0
stick = deque([64])
while True:
    if sum(stick) == X:
        print(len(stick))
        break
    x = stick.popleft()
    x //= 2
    stick.appendleft(x)
    if sum(stick) < X:
        stick.appendleft(x)


