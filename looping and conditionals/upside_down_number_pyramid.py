n=12345678987654321
for i in range((len(str(n))//2)+1):
    print(i*" ",n,sep="")
    n = n//10
    n = n%(10**(len(str(n))-1))
