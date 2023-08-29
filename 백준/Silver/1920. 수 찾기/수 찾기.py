import sys

N = int(input())
A = list(map(int, input().split()))
M = int(input())
find_list = list(map(int, input().split()))

A.sort()

for i in find_list:
    low = 0
    high = N - 1

    while True:
        mid = (high + low) // 2
        if A[mid] == i:
            print(1)
            break

        if low >= high:
            print(0)
            break

        if A[mid] < i:
            low = mid + 1

        elif A[mid] > i:
            high = mid - 1


