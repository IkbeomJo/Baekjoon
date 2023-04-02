T = int(input())
change = [0, 0, 0, 0]
coin = [25, 10, 5, 1]
for _ in range(T):
    money = int(input())
    for i in range(4):
        empty = money // coin[i]
        change[i] = empty
        empty *= coin[i]
        money -= empty
    print(*change)
