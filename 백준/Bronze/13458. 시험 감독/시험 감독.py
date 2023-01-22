import math
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0
for i in A:
    x = i - B
    cnt += 1
    if x > 0:
        cnt += math.ceil(x/C)

print(cnt)