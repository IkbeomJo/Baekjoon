A = list()
max_index = 0
for i in range(9):
    A.append(int(input()))
    if(A[i]>A[max_index]):
        max_index = i

print(A[max_index], max_index+1)
    