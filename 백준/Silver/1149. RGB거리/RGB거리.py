n = int(input())
price_List = list()

for i in range(n):
    price_List.append(list(map(int, input().split())))

for i in range(1,n):
    price_List[i][0] = price_List[i][0] + min(price_List[i-1][1] , price_List[i-1][2])
    price_List[i][1] = price_List[i][1] + min(price_List[i-1][0] , price_List[i-1][2])
    price_List[i][2] = price_List[i][2] + min(price_List[i-1][0] , price_List[i-1][1])

print(min(price_List[n-1]))


