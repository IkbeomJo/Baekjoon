def fib(n):
    global cnt
    cnt += 1
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input())
global cnt
cnt = 0

fib(n)

print(cnt//2+1,n-2)