lis=[2,4,6,8,10]
count,c=1,0
for i in range(0,len(lis)):
    if i%2==0:
        print(lis[-count],end=" ")
        count=count+1
    else:
        print(lis[c],end=" ")
        c+=1
