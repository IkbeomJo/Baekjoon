P_arr = [1,1,1]

for i in range(3,101):
    P_arr.append(P_arr[i-2] + P_arr[i-3])

T = int(input())

for i in range(T):
    N = int(input())
    print(P_arr[N-1])