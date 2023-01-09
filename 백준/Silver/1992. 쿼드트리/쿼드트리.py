N = int(input())
img = list()
for _ in range(N):
    img.append(input())
result = list()
def div_img(x,y,N):
    for i in range(x,N+x):
        for j in range(y,N+y):
            if img[x][y] != img[i][j]:
                result.append('(')
                div_img(x, y, N//2)
                div_img(x, y + N//2, N//2)
                div_img(x + N//2, y, N//2)
                div_img(x + N//2, y + N//2, N//2)
                result.append(')')
                return
    if img[x][y] == '1':
        result.append('1')
    elif img[x][y] == '0':
        result.append('0')


div_img(0,0,N)

print("".join(result))