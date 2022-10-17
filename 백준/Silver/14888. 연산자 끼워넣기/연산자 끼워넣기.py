def back(L, S, depth, value):
    global min_v, max_v
    if depth == len(L) - 1:
        if value < min_v:
            min_v = value

        if value > max_v:
            max_v = value
        return

    depth += 1

    for i in range(len(S)):
        if S[i]:
            if i == 0:
                value += L[depth]
                S[i] -= 1
                back(L, S, depth, value)
                S[i] += 1
                value -= L[depth]

            elif i == 1:
                value -= L[depth]
                S[i] -= 1
                back(L, S, depth, value)
                S[i] += 1
                value += L[depth]

            elif i == 2:
                value *= L[depth]
                S[i] -= 1
                back(L, S, depth, value)
                S[i] += 1
                value = int(value / L[depth])

            elif i == 3:
                value = int(value / L[depth])
                S[i] -= 1
                back(L, S, depth, value)
                S[i] += 1
                value *= L[depth]


N = int(input())
L = list(map(int, input().split()))
S = list(map(int, input().split()))
global min_v, max_v
min_v = 1000000000
max_v = -1000000000

back(L, S, 0, L[0])
print(max_v)
print(min_v)