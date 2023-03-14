word = input()
half = len(word) // 2
if len(word) % 2:
    if word[0:half] == word[:half:-1]:
        print(1)
    else:
        print(0)
else:
    if word[0:half] == word[:half-1:-1]:
        print(1)
    else:
        print(0)
