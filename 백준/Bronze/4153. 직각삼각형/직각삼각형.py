while True:
    L = list(map(int,input().split(" ")))
    x = max(L)
    if x==0:
        break
    L.remove(x)
    if x**2 == L[0]**2 + L[1]**2:
        print("right")
    else:
        print("wrong")