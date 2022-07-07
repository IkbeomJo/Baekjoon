N = int(input())

def Fibonacci(num):
    if(num<=1):
        return num
    return Fibonacci(num-1) + Fibonacci(num-2)

print(Fibonacci(N))