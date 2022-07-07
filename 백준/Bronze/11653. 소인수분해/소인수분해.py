N = int(input())
d = 2
while N>=d:
    if N%d == 0:
        N /= d
        print(d)
    else:
        d+=1

