T = int(input())


for i in range(T):
    S = list(map(str,input().split()))
    for j in range(len(S[1])):
        for z in range(int(S[0])):
            print(S[1][j],end="")
    print("")
        