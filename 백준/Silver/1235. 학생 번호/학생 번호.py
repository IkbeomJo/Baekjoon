N = int(input())
std_list = list()
for i in range(N):
    std_list.append(input())
std_len = len(std_list[0])
for i in range(1,std_len+1):
    new_std_list = list()
    for j in range(len(std_list)):
        new_std_list.append(std_list[j][std_len-i:std_len])
    x = set(new_std_list)
    if len(x) == len(new_std_list):
        print(i)
        break
