N = int(input())
sum_v = 1
def factorial(num):
    global sum_v
    if(num==0):
        return sum_v
    else:
        sum_v*=num
        num-=1
        return factorial(num)

result = factorial(N)
print(result)