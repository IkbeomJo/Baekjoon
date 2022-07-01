H, M = map(int,input().split())
T = int(input())

if(M+ (T%60)>=60):
    H+= T/60 +1
    M+= T%60 - 60
    H%=24
    print(int(H), M)
else:
    H+= T/60
    M+= T%60
    H%=24
    print(int(H), M)