import sys
from collections import deque

T = int(input())

for _ in range(T):
    R_cnt = 0
    p = input()
    n = int(input())
    AC_list = deque(input().strip("[]").split(","))
    if not n:
        AC_list = deque([])
    for i in range(len(p)):
        if p[i] == 'D' and not len(AC_list):
            print("error")
            break

        elif p[i] == 'D' and R_cnt % 2 == 0:
            AC_list.popleft()

        elif p[i] == 'D' and R_cnt % 2 == 1:
            AC_list.pop()

        elif p[i] == 'R':
            R_cnt += 1

        if i == len(p)-1 and not len(AC_list):
            print("[]")

        elif i == len(p)-1 and not R_cnt % 2:
            print("[",end="")
            for i in range(len(AC_list)):
                if i == len(AC_list)-1:
                    print(AC_list[i],end="")
                else:
                    print(AC_list[i],end=',')
            print("]")

        elif i == len(p)-1 and R_cnt % 2:
            AC_list.reverse()
            print("[", end="")
            for i in range(len(AC_list)):
                if i == len(AC_list) - 1:
                    print(AC_list[i], end="")
                else:
                    print(AC_list[i], end=',')
            print("]")
