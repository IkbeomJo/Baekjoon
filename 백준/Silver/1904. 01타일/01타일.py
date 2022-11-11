def countBin(n):
    if n<3:
        return bin_L[n]
    else:
        for i in range(3, n+1):
            bin_L[i] = (bin_L[i-1] + bin_L[i-2])%15746

        return bin_L[n]

n = int(input())
bin_L = [0]

bin_L = [0 for _ in range(n+1)]
bin_L[1] = 1
if n>1:
    bin_L[2] = 2

print(countBin(n))

