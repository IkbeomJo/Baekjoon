N, M = map(int, input().split())
basket = [i for i in range(1,N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    temp_list = basket[i-1:j]
    temp_list.reverse()
    for x in range(len(temp_list)):
        basket[i-1+x] = temp_list[x]
print(*basket)