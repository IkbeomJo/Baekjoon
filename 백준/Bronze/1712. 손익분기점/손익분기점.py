A, B, C = map(int, input().split())
if(B>=C):
    print("-1")
else:
    margin_price = C-B
    breakeven_Point = int(A/margin_price) + 1
    print(breakeven_Point)