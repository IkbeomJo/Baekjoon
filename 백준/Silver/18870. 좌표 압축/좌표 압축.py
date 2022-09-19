N = int(input())

L = list(map(int, input().split(" ")))

L_s = set(L)

L_s = sorted(L_s)


dic = {L_s[i] : i for i in range(len(L_s))}

for i in L:
    print(dic[i],end=" ")
    
