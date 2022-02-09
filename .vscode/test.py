n=int(input())
count=0
temp=n
temp_2=temp%5
while True:
    if temp%5==0:
        count=temp//5
        print(count)
        break
    if temp_2%3==0:
        count=count+temp//5
        temp=temp-count*5
        if temp%3==0:
            while temp!=0:
                temp=temp-3
                count=count+1
        print(count)
        break
    if temp_2%3!=0:
        if temp%3==0 and temp<15:
            while temp!=0:
                temp=temp-3
                count=count+1
            print(count)
            break
        temp-=5
        count+=1
        if temp<3:
            print(-1)
            break
        if temp==0:
            print(count)
            break

        
   


    
   