N = int(input())
cnt = 0
UseEmoji = set()
for _ in range(N):
    text = input()
    if text == "ENTER":
        UseEmoji = set()
        continue

    if text not in UseEmoji:
        UseEmoji.add(text)
        cnt += 1

print(cnt)