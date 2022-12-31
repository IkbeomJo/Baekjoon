A,B = input().split()
diff_len = len(B) - len(A) +1
min_cnt = 51
for i in range(diff_len):
    cnt = 0
    for j in range(len(A)):
        if B[i+j] != A[j]:
            cnt += 1
    if min_cnt>cnt:
        min_cnt = cnt

print(min_cnt)

