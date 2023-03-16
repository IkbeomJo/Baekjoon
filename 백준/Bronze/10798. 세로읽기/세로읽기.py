border = []
max_len = 0
for i in range(5):
    border.append(list(input()))
    if len(border[i]) > max_len: max_len = len(border[i])

for i in range(max_len):
    for j in range(5):
        if len(border[j]) > i: print(border[j][i],end='')