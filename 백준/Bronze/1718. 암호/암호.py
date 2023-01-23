word = input()
password = input()
index = 0

for i in range(len(word)):
    x = 97 - ord(word[i])
    y = 97 - ord(password[index])
    if index == len(password)-1:
        index = 0
    else:
        index += 1
    if word[i] == " ":
        print(" ",end='')
    elif y > x:
        print(chr(97 + (y - x - 1)),end='')
    else:
        print(chr(122 - abs(y - x)),end='')





