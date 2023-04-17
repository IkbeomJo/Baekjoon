import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
wordBook = dict()

for _ in range(N):
    word = input().rstrip()
    if len(word) < M: continue


    if word not in wordBook:
        wordBook[word] = 1
    else:
        wordBook[word] = wordBook[word] + 1


wordBook = sorted(wordBook.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))
for i in wordBook:
    print(i[0])
