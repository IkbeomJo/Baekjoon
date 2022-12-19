import sys

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
find_A = list(map(int, input().split()))

for i in find_A:
    start = 0
    end = len(A) - 1
    mid = len(A) // 2

    while True:
        if i > A[mid]:
            start = mid
            mid = (start + end) // 2

        elif i < A[mid]:
            end = mid
            mid = (start + end) // 2


        if A[mid] == i or A[mid+1] == i:
            print(1)
            break
        elif start == mid or end == mid:
            print(0)
            break


