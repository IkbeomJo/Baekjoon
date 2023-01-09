N = int(input())
paper = list()
for _ in range(N):
    paper.append(list(map(int, input().split(' '))))
cnt_int = [0,0,0]
def div_paper(x,y,N):
    for i in range(x,N+x):
        for j in range(y,N+y):
            if paper[x][y] != paper[i][j]:
                for a in range(3):
                    for b in range(3):
                        div_paper(x + N//3 * a, y + N//3 * b, N//3)

                return

    cnt_int[paper[x][y]+1] += 1

div_paper(0,0,N)

for i in cnt_int:
    print(i)