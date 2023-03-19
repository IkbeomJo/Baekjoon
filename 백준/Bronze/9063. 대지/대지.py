n = int(input())
x_grid = list()
y_grid = list()
for _ in range(n):
    x, y = map(int, input().split())
    x_grid.append(x)
    y_grid.append(y)

print((max(x_grid) - min(x_grid)) * (max(y_grid) - min(y_grid)))
