T = int(input())
result = set()
for _ in range(T):
    name, log = input().split()
    if log == "enter":
        result.add(name)
    else:
        result.remove(name)

result = list(result)
result.sort(reverse=True)
for i in result:
    print(i)