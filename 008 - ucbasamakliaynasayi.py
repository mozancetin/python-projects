a=[]
b=0
while(True):

    if b!=1000:
        b+=1
        x=b-(b//10)*10
        y=(b//10)-((b//10)//10)*10
        z=int((b//10)-y)/10
        
        if x == z :
            a.append(b)
    else:
        print(a)
        break
        
    
input()
