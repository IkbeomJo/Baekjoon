N = int(input())

for i in range(N):
    count = 1
    S = input()
    i, r = 0, len(S)-1
    while i < r-i:
        if S[i] != S[r-i]:
            print(0,end=" ")
            break
        elif S[i] == S[r-i]:
            count += 1
            i += 1
    if i >= r-i:
        print(1,end=" ")
    print(count)
    