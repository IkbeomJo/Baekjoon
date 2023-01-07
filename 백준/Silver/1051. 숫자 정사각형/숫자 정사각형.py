N, M = map(int, input().split())
square = list()
for _ in range(N):
    square.append(input())
break_division = False
max_square = 1

for i in range(1,min(N,M)):
    for x in range(N-i):
        for y in range(M-i):
            if square[x][y] == square[x+i][y] == square[x][y+i] == square[x+i][y+i]:
                max_square = i+1
                break_division = True
                break
        if break_division:
            break
    break_division = False

print(max_square**2)

