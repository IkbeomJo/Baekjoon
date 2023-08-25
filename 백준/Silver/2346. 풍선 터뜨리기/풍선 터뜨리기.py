import collections

N = int(input())
balloon = collections.deque(range(1,N+1))
order = collections.deque(list(map(int,input().split(' '))))
result = list()
for i in range(N):
    order_value = order.popleft()
    result.append(balloon.popleft())
    if len(order) == 0: break
    if order_value > 0:
        for j in range(order_value-1):
            balloon.append(balloon.popleft())
            order.append(order.popleft())
    elif order_value < 0:
        for j in range(abs(order_value)):
            balloon.appendleft(balloon.pop())
            order.appendleft(order.pop())
print(*result)