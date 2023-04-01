N, B = map(int, input().split())
result = list()
while True:
    if N // B == 0: break
    result.append(N % B)
    N //= B
result.append(N)
result.reverse()

for i in result:
    if i < 10: print(i,end='')
    else: print(chr(55+i),end='')
