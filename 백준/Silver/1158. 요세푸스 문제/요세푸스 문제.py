N, K = map(int, input().split())
Josephus = [i for i in range(1,N+1)]
empty = list()
result = list()
search_index = 0
while True:
    for _ in range(K):
        if len(Josephus) > search_index:
            search_index += 1
        else:
            search_index = 1
            for i in empty:
                Josephus.remove(i)
                result.append(i)
            empty.clear()

    if len(Josephus) == 0:
        break
    empty.append(Josephus[search_index-1])


print('<',end='')
for i in range(len(result)-1):
    print(result[i],end=', ')
print(f"{result[-1]}>")

