#Tahmin ettiğiniz sayıyı en fazla 7 hamlede bulur
import random
c=1
a=1
b=100
while(True):
    tahmin=int((a+b)/2)
    print("\n" , "Tahminim:" , tahmin , "doğru mu? \n")
    bkmk=int(input(" Daha büyükse: 1 \n Daha küçükse: -1 \n Bildiyse:0 yazın \n "))
    if bkmk==0:
        print(c,"adımda bildim!")
        break
    elif bkmk==1:
        a=tahmin
        c=c+1
    elif bkmk==-1:
        b=tahmin
        c=c+1
input()
