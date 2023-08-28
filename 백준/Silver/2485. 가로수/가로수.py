import sys
from math import gcd

N = int(input())
distance = list()
distance_between = list()
for _ in range(N):
    distance.append(int(sys.stdin.readline()))

for i in range(1,N):
    distance_between.append(distance[i]-distance[i-1])

g = distance_between[0]
for j in range(1, N-1):
    g = gcd(g, distance_between[j])

result = (distance[-1] - distance[0]) // g

print(result - N + 1)