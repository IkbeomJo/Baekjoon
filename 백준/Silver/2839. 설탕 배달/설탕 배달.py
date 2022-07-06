N = int(input())

bag = 0

if N % 5 == 0:
    bag += N/5
    print(int(bag))
else:
    while N>0:
        N-=3
        bag+=1
        if N%5 == 0:
            bag += N/5
            print(int(bag))
            break
        
        elif N==1 or N==2:
            print("-1")
            break
            
        elif N==0:
            print(int(bag))
            break