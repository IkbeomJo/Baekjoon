x_L =list()
y_L =list()
for _ in range(3):
    x, y = map(int,input().split(" "))
    if x in x_L:
        x_L.remove(x)
    else:
        x_L.append(x)
    if y in y_L:
        y_L.remove(y)
    else:
        y_L.append(y)

print(x_L[0],y_L[0])