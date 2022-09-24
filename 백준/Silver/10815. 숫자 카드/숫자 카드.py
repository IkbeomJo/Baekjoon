N = int(input())
S = set(map(int,input().split(" ")))
M = int(input())
L = list(map(int, input().split(" ")))

for i in L:
    result = i in S
    if result == True:
        print("1",end=" ")
    elif result == False:
        print("0",end=" ")