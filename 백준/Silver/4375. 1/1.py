while True:
    try:
        n = int(input())
        cnt = 0
        while True:
            cnt += 1
            one = '1' * cnt
            one = int(one)
            if one % n == 0:
                print(cnt)
                break
    except:
        break