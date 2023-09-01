import collections
import sys
result = 0
N, C = map(int, input().split())
home_location = list()
for _ in range(N):
    home_location.append(int(sys.stdin.readline()))
home_location.sort()
low, high = 1, home_location[-1]-home_location[0]

while low <= high:
    mid = (low+high) // 2
    cnt = 1
    Cumulative_sum = 0
    for i in range(1, N):
        if Cumulative_sum + home_location[i] - home_location[i-1] >= mid:
            cnt += 1
            Cumulative_sum = 0
        else:
            Cumulative_sum += home_location[i] - home_location[i-1]

    if cnt >= C:
        low = mid + 1
        result = mid

    elif cnt < C:
        high = mid - 1

print(result)