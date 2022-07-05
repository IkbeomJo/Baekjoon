N = int(input())
A = 1
count = 1

while True:
    if N<=A:
        break
    A = A+(6*count)
    count += 1
    
print(count)