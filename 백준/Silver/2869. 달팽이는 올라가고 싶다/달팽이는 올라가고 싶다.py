import math
A, B, V = map(int,input().split())
S= A-B
N= V-B

print(math.ceil(N/S))