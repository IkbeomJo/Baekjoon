N, L = map(int, input().split())
result = list()
while L < 101:
    if L % 2 == 1 and N / L == N // L:
        for i in range(1, L // 2 + 1):
            result.append(N//L - i)
            result.append(N // L + i)
        result.append(N//L)
        break

    elif L % 2 == 0 and N / L == N // L + 0.5:
        for i in range(L//2-1,-1,-1):
            result.append(N // L - i)
            result.append(N // L + i+1)
        break

    else:
        L += 1

result.sort()
if len(result) == 0 or result[0] < 0:
    print(-1)
else:
    print(*result)



