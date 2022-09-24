S = input()
L = set()
for i in range(1, len(S)+1):
    for j in range(len(S)-i+1):
        x = S[j:j+i]
        if x in L:
            continue
        else:
            L.add(x)
print(len(L))
            