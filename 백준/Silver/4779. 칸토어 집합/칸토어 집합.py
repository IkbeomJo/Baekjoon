def kantour(x):
    if x == 0 or x == 1: print("-",end='')
    else:
        kantour(x // 3)
        print(" "*(x//3),end="")
        kantour(x // 3)

while True:
    try:
        N = int(input())
        x = 3**N
        kantour(x)
        print("")
    except EOFError:
        break