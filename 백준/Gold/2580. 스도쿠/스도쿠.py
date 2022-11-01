def Sudoku(L):
    sudoku_arr = L
    zero_index = list()
    n = 0

    for i in range(9):
        for j in range(9):
            if sudoku_arr[i][j] == 0:
                zero_index.append([i, j])

    def back(n):
        if n == len(zero_index):
            for i in range(9):
                print(*sudoku_arr[i])
            exit(0)
            return

        row = zero_index[n][0]
        col = zero_index[n][1]

        for i in range(1, 10):

            if is_possible(n,i):
                sudoku_arr[row][col] = i
                back(n + 1)
                sudoku_arr[row][col] = 0


    def is_possible(n,val):
        row = zero_index[n][0]
        col = zero_index[n][1]

        for i in range(9):
            if val == sudoku_arr[row][i] or val == sudoku_arr[i][col] or val == sudoku_arr[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3]:
                return False

        return True

    back(n)

L = list()
for _ in range(9):
    L.append(list(map(int,input().split())))

Sudoku(L)