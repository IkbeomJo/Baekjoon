chess_board = list()
cnt = 0
for _ in range(8):
    chess_board.append(input())

for i in range(8):
    for j in range(8):
        if not (i+j) % 2 and chess_board[i][j] == 'F':
            cnt += 1

print(cnt)
