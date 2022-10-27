L = list()
for i in range(5):
    L.append(int(input()))

L.sort()

if len(L) % 2:
    med = L[len(L)//2]
else:
    med = L[len(L)//2]+L[len(L)//2-1]//2

avg = sum(L)//len(L)

print(avg)
print(med)