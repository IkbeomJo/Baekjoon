N = int(input())
str_list = list()
result = list()
for _ in range(N):
    str_list.append(input())

for i in range(len(str_list[0])):
    for j in range(1,N):
        if str_list[j][i] != str_list[0][i]:
            result.append('?')
            break
    if len(result) == i:
        result.append(str_list[0][i])

result = "".join(result)
print(result)