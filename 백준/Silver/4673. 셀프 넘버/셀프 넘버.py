def d(n):
    sum_v=n
    x = str(n)
    for i in range(len(x)):
        sum_v += int(x[i])
    return sum_v

a = set(range(1,10001))
b = set()

for i in range(1,10001):
    b.add(d(i))

self_num = sorted(a-b)
for i in range(len(self_num)):
    print(self_num[i])