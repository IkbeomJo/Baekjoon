from collections import deque
N, M = map(int, input().split())
basket = [i for i in range(1,N+1)]

for _ in range(M):
    i, j, k = map(int, input().split())
    empty = deque(basket[i-1:j])
    for _ in range(k-i):
        empty.append(empty.popleft())
    basket[i-1:j] = empty

print(*basket)

