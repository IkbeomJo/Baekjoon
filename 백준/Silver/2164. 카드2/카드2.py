import sys
from collections import deque
N = int(input())
deck = deque(i for i in range(N,0,-1))
input_Mod = False

while len(deck) != 1:
    if input_Mod:
        deck.appendleft(deck.pop())
        input_Mod = False
    else:
        deck.pop()
        input_Mod = True

print(deck[0])
