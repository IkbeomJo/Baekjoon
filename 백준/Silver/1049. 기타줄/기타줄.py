N, M = map(int, input().split())
min_each = 1000
min_pack = 1000
for i in range(M):
    x,y = map(int, input().split())
    if y*6 < x:
        x = y*6
    if min_pack > x:
        min_pack = x
    if min_each > y:
        min_each = y

remained_N = N % 6
result = N // 6 * min_pack
if remained_N * min_each > min_pack:
    print(result + min_pack)
else:
    print(result + min_each * remained_N)


