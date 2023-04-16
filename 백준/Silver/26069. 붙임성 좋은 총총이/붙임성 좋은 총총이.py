n = int(input())
Dancing_list = set()
Dancing_list.add("ChongChong")
for _ in range(n):
    People1, People2 = input().split()
    if People1 in Dancing_list or People2 in Dancing_list:
        Dancing_list.add(People1)
        Dancing_list.add(People2)

print(len(Dancing_list))