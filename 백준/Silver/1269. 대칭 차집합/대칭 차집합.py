a, b = map(int, input().split(" "))
a = set(map(int, input().split(" ")))
b = set(map(int, input().split(" ")))
x = a-b
y = b-a
print(len(x)+len(y))