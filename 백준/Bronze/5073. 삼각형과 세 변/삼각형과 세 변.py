while True:
    triangle = list(map(int, input().split()))
    triangle.sort(reverse=True)
    if sum(triangle) == 0: break
    elif triangle[0] >= triangle[1] + triangle[2]: print("Invalid")
    elif triangle[0] == triangle[1] == triangle[2]: print("Equilateral")
    elif triangle[0] != triangle[1] != triangle[2]: print("Scalene ")
    else: print("Isosceles")
