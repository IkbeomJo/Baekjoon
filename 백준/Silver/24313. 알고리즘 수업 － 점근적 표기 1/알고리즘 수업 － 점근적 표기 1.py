a, b = map(int, input().split())
c = int(input())
n = int(input())
for i in range(n,101):
    if a*i + b > c * i:
        print(0)
        exit(0)
print(1)