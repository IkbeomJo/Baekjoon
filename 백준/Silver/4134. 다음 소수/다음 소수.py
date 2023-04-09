import sys
import math
input = sys.stdin.readline

def isPrime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True


T = int(input())
for _ in range(T):
    x = int(input())
    while not isPrime(x):
        x += 1

    print(x)
