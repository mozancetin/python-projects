n=10000
i=100
a=0
s=0
while(n<998001):
    if str(n)==str(n)[::-1]:
        if i<=999:
            if n%i==0:
                b = n / i #bölüm
                if len(str(int(b)))==3:
                    ebs=n
                    a=b #bölüm
                    s=i #bölen
                    n+=1
                else:
                    n+=1        
            else:
                
                i+=1
        else:
            n+=1
            i=100
    else:
        n+=1
print("3 Haneli 2 sayıdan oluşan en büyük palindrom sayı:",ebs,"\nÇarpanları:",int(a),",",s)
input()

