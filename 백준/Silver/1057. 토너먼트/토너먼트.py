N, Jimin, hansu = map(int, input().split())
cnt = 0
while Jimin != hansu:
    Jimin -= Jimin//2
    hansu -= hansu//2
    cnt += 1
print(cnt)