N = int(input())
A = list(map(int, input().split()))
LIS_List = [0]


for i in A:
    if LIS_List[-1] < i:
        LIS_List.append(i)
    else:
        low, high = 0, len(LIS_List)

        while low < high:
            mid = (low + high) // 2
            if LIS_List[mid] < i:
                low = mid + 1
            else:
                high = mid
        LIS_List[high] = i

print(len(LIS_List)-1)