while True:
    x = input()
    cnt = 0
    if x == '0':
        break

    while True:
        if len(x) % 2:
            i = x[:len(x) // 2]
            j = x[:len(x) // 2:-1]
        else:
            i = x[:len(x) // 2]
            j = x[-1:len(x)//2-1:-1]
        if i == j:
            break
        length = len(x)
        x_temp = str(int(x)+1)
        x = '0'*(length-len(x_temp)) + x_temp
        cnt+=1

    print(cnt)

