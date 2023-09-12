T = int(input())
for _ in range(T):
    N = int(input())
    max_drink = 0
    for _ in range(N):
        university, drink = input().split()
        drink = int(drink)
        if max_drink < drink:
            result = university
            max_drink = drink

    print(result)