N = int(input())

def test(num):
    if num == 1:
        return("*")
    stars = test(num//3)
    L = list()
    for star in stars:
        L.append(star*3)
    for star in stars:
        L.append(star+' '*(num//3)+star)
    for star in stars:
        L.append(star*3)
    
    return L

print('\n' .join(test(N)))
                 