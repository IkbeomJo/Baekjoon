n = int(input())

wine_list = [0]
wine_prefix_list = [0 for _ in range(n+1)]
for i in range(n):
    wine_list.append(int(input()))

wine_prefix_list[1] = wine_list[1]

if n>1:
    wine_prefix_list[2] = wine_list[1] + wine_list[2]

for i in range(3, n+1):
    wine_prefix_list[i] = max(wine_prefix_list[i-3] + wine_list[i-1] + wine_list[i],
                              wine_prefix_list[i-2] + wine_list[i],
                              wine_prefix_list[i-1])

print(wine_prefix_list[n])