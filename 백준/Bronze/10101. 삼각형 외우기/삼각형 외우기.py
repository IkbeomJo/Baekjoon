x = int(input())
y = int(input())
z = int(input())

if x == 60 and y == 60 and z == 60: print("Equilateral")
elif x + y + z == 180 and x == y or y == z or z == x: print("Isosceles")
elif x + y + z == 180: print("Scalene")
else: print("Error")