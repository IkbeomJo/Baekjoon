def findminS(S, C, C_all, N,x):
    global min_v
    if len(C) == N // 2:
        start = list(C)
        link = list(C_all - C)
        Start_sum = 0
        link_sum = 0
        for x in range(N // 2):
            for y in range(N // 2):
                Start_sum += S[start[x] - 1][start[y] - 1]
                link_sum += S[link[x] - 1][link[y] - 1]
        value = abs(Start_sum - link_sum)
        if value < min_v:
            min_v = value
        return

    for i in range(x, N + 1):
        if i in C:
            C.remove(i)
            findminS(S, C, C_all, N,i+1)
            C.add(i)


N = int(input())
S = list()
for i in range(N):
    S.append(list(map(int,input().split())))

C = {i for i in range(1, N + 1)}
C_all = {i for i in range(1, N + 1)}
global min_v
min_v = 99999999999999
findminS(S, C, C_all, N,1)

print(min_v)