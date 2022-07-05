S = input().upper()
count_s = 0
ID = list(set(S))
max_count = 0
max_value = 0

for i in range(len(ID)):
    count_temp = 0 
    for j in range(len(S)):
        if(ID[i]==S[j]):
            count_temp += 1
    if(count_s < count_temp):
        max_count = 1
        max_value = ID[i]
        count_s = count_temp
    elif(count_s == count_temp):
        max_count += 1

if(max_count == 1):
    print(max_value)
elif(max_count>1):
    print("?")