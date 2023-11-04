for i in range(1,1001):
    if len(str(i))==3:
        if i%10 + (i%100)//10 + (i%1000)//100 == 20:
            print(i)
    if len(str(i))==4:
        if i%10 + (i%100)//10 + (i%1000)//100 + (i%10000)//1000 == 20:
            print(i)
