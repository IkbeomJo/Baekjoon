N, Tesu_score, P = map(int, input().split())
if N >0:
    score_list = list(map(int, input().split()))
else:
    print(1)
    exit(0)

score_list.append(Tesu_score)
score_list.sort(reverse=True)
x = score_list.index(Tesu_score) + 1

if x > P:
    print(-1)
else:
    if N == P and Tesu_score == score_list[-1]:
        print(-1)
    else:
        print(x)
        