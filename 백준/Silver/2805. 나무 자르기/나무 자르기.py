N, M = map(int, input().split())
tree_height = list(map(int, input().split()))

low, high = 0, max(tree_height)
max_value = 0

while low<=high:
    mid = (low+high) // 2
    cumulative_height = 0
    for i in range(N):
        if tree_height[i] > mid:
            cumulative_height += tree_height[i] - mid

    if cumulative_height >= M and max_value <= mid:
        max_value = mid

    if cumulative_height < M:
        high = mid - 1
    elif cumulative_height >= M:
        low = mid + 1





print(max_value)