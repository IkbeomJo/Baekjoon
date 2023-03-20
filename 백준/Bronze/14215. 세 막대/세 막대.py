x = list(map(int, input().split()))
x.sort(reverse=True)
y = x[1] + x[2]
if y <= x[0]: x[0] = y-1
print(sum(x))