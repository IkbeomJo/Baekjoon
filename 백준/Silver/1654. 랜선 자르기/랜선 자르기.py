K, N = map(int, input().split())
line = list()
for _ in range(K):
    line.append(int(input()))

low = 1
high = max(line)
while low <= high:
    mid = (high + low) // 2
    cut_line = 0
    for i in line:
        cut_line += i // mid
    if cut_line >= N:
        low = mid + 1
    else:
        high = mid - 1

print(high)



