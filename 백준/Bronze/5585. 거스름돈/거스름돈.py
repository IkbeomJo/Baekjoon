N = int(input())
money = [500, 100, 50, 10, 5, 1]
cnt = 0
N = 1000 - N
while N != 0:
    for i in money:
        while N >= i:
            N -= i
            cnt += 1

print(cnt)