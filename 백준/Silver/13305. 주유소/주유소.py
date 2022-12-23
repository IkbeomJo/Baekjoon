N = int(input())
city_distance = list(map(int, input().split()))
price_list = list(map(int, input().split()))
total_oli = 0
i = 0
while i < N-1:
    if price_list[i+1] < price_list[i]:
        total_oli += price_list[i] * city_distance[i]
        i += 1
    elif price_list[i+1] >= price_list[i]:
        empty_distance = city_distance[i]
        price_list[i+1] = price_list[i]
        i += 1
        while i < N-1:

            if price_list[i+1] < price_list[i]:
                break

            elif price_list[i+1] >= price_list[i]:
                empty_distance += city_distance[i]
                price_list[i+1] = price_list[i]
                i += 1

        total_oli += empty_distance * price_list[i]
print(total_oli)