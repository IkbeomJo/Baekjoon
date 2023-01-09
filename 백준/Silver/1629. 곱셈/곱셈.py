A, B, C = map(int , input().split())

def div(A, B, C):
    if B >= 2:
        x = div(A, B//2, C)
        if B % 2:
            return x * x * A % C
        else:
            return x * x % C
    else:
        return A % C

print(div(A,B,C))

