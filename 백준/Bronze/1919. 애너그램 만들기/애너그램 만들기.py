A = input()
B = input()
A_list = [0 for _ in range(26)]
B_list = [0 for _ in range(26)]
for i in range(len(A)):
    A_list[97-ord(A[i])] += 1
for i in range(len(B)):
    B_list[97-ord(B[i])] += 1
cnt = 0
for i in range(26):
    cnt += abs(A_list[i]-B_list[i])
print(cnt)
