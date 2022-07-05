A,B = input().split()
X = [int(A[::-1]),int(B[::-1])]
if(X[0]>X[1]):
    print(X[0])
else:
    print(X[1])
