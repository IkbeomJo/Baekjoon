P = int(input())
for _ in range(P):
    work_cnt = 0
    line = list(map(int, input().split()))
    for i in range(2, 21):
        for j in range(1,i):
            if line[j] > line[i]:
                line.insert(j,line.pop(i))

                work_cnt += i-j
                break
    print(line[0], work_cnt)
