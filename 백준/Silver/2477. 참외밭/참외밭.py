K = int(input())

L = list()
h_max = [0,0]
w_max = [0,0]

for _ in range(6):
    D, R = map(int,input().split(" "))
    L.append([R,D])

for i in range(6):
    if L[i][1] == 3 or L[i][1] == 4:
        if L[i][0] > w_max[0]:
            w_max[0] = L[i][0] 
            w_max[1] = i
    else:
        if L[i][0] > h_max[0]:
            h_max[0] = L[i][0]
            h_max[1] = i

if w_max[1] == 0:
    w_min = abs(L[5][0] - L[1][0])
elif w_max[1] == 5:
    w_min = abs(L[4][0] - L[0][0])
else:
    w_min = abs(L[w_max[1]-1][0] - L[w_max[1]+1][0])

if h_max[1] == 0:
    h_min = abs(L[5][0] - L[1][0])
elif h_max[1] == 5:
    h_min = abs(L[4][0] - L[0][0])
else:
    h_min = abs(L[h_max[1]-1][0] - L[h_max[1]+1][0])
    
min_area = w_min * h_min          
area = w_max[0] * h_max[0]


print(K * (area - min_area))
