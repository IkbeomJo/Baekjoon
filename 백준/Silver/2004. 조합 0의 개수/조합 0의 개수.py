def count(V, N):
    cnt = 0
    while V:
        V = V // N
        cnt += V
    return cnt

n, m = map(int, input().split())
five_num = count(n, 5) - count(m, 5) - count(n-m, 5)
two_num = count(n, 2) - count(m, 2) - count(n-m, 2)

print(min(five_num,two_num))