S = input()
time = 0

L = [['A','B','C'],['D','E','F'],['G','H','I'],
     ['J','K','L'],['M','N','O'],['P','Q','R','S'],
     ['T','U','V'],['W','X','Y','Z']]

for i in range(len(S)):
    for j in range(len(L)):
        for z in L[j]:
            if(S[i]== z):
                time += (j+3)
print(time)
            