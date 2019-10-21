n=2
i=2
c=1
while(c!=10002):
    if n<i**2 :
        ebs=n
        n+=1
        c+=1
        i=2
    if int(n/i)*i==n :
        n+=1
        i=2
    else:
        if int(i/2)*2==i :
            i=i+1
        else:
            i=i+2
print("10001. asal sayı:",ebs)
input()
