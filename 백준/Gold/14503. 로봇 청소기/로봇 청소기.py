N, M = map(int, input().split())
r,c,d = map(int, input().split())
clean_map = [[1 for _ in range(M+2)]]
for i in range(N):
    clean_map.append(list(map(int, input().split())))

for i in range(1,N+1):
    clean_map[i].insert(0,1)
    clean_map[i].append(1)
clean_map.append([1 for _ in range(M+2)])


cnt = 0
r,c = r+1, c+1

while True:
    if clean_map[r][c] == 0:
        cnt += 1
        clean_map[r][c] = 2

    if clean_map[r-1][c] == 0 or clean_map[r][c+1] == 0 or clean_map[r+1][c] == 0 or clean_map[r][c-1] == 0:
        if d == 0: d = 3
        else: d -= 1

        if d == 0 and clean_map[r-1][c] == 0:
            r,c = r-1, c
        elif d == 1 and clean_map[r][c+1] == 0:
            r,c = r,c+1
        elif d == 2 and clean_map[r+1][c] == 0:
            r,c = r+1, c
        elif d == 3 and clean_map[r][c-1] == 0:
            r,c = r, c-1
    elif clean_map[r-1][c] != 0 and clean_map[r][c+1] != 0 and clean_map[r+1][c] != 0 and clean_map[r][c-1] != 0:
        if d == 0 and clean_map[r+1][c] != 1:
            r,c = r+1,c
        elif d == 1 and clean_map[r][c-1] != 1:
            r,c = r, c-1
        elif d == 2 and clean_map[r-1][c] != 1:
            r,c = r-1,c
        elif d == 3 and clean_map[r][c+1] != 1:
            r,c = r,c+1
        else:
            break

print(cnt)
