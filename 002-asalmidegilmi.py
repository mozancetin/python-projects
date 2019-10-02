n=int(input("\nAsal sayı olup olumadığını sorgulamak istediğiniz sayıyı girin: "))
i=2
while(True):
    if n<i**2 :
        print("Asal sayı")
        break
    if int(n/i)*i==n :
        print("Asal sayı değil")
        break
    else:
        if int(i/2)*2==i :
            i=i+1
        else:
            i=i+2
input()
