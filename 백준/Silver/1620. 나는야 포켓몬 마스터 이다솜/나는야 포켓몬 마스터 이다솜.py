import sys
N, M = map(int,input().split(" "))
D_I = dict()
D_S = dict()
for i in range(1,N+1):
    s = sys.stdin.readline().strip()
    D_I[i] = s
    D_S[s] = i

for i in range(M):
    s = sys.stdin.readline().strip()
    if ord(s[0]) >= 48 and ord(s[0]) <= 57:
        print(D_I[int(s)])
    else:
        print(D_S[s])
    