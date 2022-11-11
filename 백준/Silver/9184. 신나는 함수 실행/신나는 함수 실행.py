def w(a,b,c):
    if abc_arr[a][b][c] == 0:
        if a<b<c:
            abc_arr[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        else:
            abc_arr[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)

        return abc_arr[a][b][c]

    else:
        return abc_arr[a][b][c]

while True:
    a,b,c = map(int, input().split())
    p_a, p_b,p_c = a, b, c
    if a == b == c == -1:
        break

    elif a<=0 or b<=0 or c<=0:
        a,b,c = 0,0,0
        
    elif a>20 or b > 20 or c >20:
        a,b,c  = 20, 20, 20


    abc_arr = [[[0 for _ in range(c+3)]for _ in range(b+3)]for _ in range(a+3)]
    for i in range(a+1):
        for j in range(b+1):
            for z in range(c+1):
                if i == 0 or j == 0 or z == 0:
                    abc_arr[i][j][z] = 1

    print(f"w({p_a}, {p_b}, {p_c}) = {w(a,b,c)}")