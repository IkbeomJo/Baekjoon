S1, S2, S3 = map(int, input().split())
dice = [0 for i in range(81)]
for i in range(1, S1+1):
    for j in range(1, S2+1):
        for z in range(1, S3+1):
            dice[i+j+z] += 1

print(dice.index(max(dice)))