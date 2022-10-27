L = list()
for i in range(1,29):
    L.append(int(input()))
for i in range(1,31):
    if i in L:
        continue
    print(i)