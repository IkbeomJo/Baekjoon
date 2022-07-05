N = int(input())
result = N
for i in range(N):
    count = 0
    S = input()
    group_word_id = set(S)
    for i in range(len(S)-1):
        if(S[i]==S[i+1]):
            continue
        else:
            count+=1
    if count != (len(group_word_id)-1):
        result -=1
print(result)