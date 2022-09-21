x, y, w, h = map(int, input().split(" "))
L = list()
L.append(x)
L.append(y)
L.append(w-x)
L.append(h-y)

print(min(L))

