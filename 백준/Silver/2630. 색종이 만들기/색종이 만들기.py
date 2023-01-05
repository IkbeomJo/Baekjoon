N = int(input())
paper = list()
for i in range(N):
    paper.append(list(map(int, input().split())))
blue = 0
white = 0
def div_paper(x, y, N):
    global blue, white
    for i in range(x,N+x):
        for j in range(y,N+y):
            if paper[x][y] != paper[i][j]:
                div_paper(x, y, N//2)
                div_paper(x + N//2, y, N//2)
                div_paper(x, y + N//2, N//2)
                div_paper(x + N//2, y + N//2, N//2)
                return
    if paper[x][y] == 1:
        blue += 1
    else:
        white += 1

div_paper(0,0,N)
print(white)
print(blue)




