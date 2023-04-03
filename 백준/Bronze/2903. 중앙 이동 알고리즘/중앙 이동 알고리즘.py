N = int(input())
x = 1
y = 2
for i in range(1,N+1):
    y += x
    x *= 2

print(y*y)