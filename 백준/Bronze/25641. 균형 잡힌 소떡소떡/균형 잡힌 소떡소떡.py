N = int(input())
L = list(input())

S_s = L.count("s")
S_t = L.count("t")

while S_s != S_t:
    x = L[0]
    
    if L[0] == "s":
        S_s = S_s - 1
    else:
        S_t = S_t - 1
    
    del L[0]
    
print("".join(L))