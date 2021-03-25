#İstediğiniz sayıdan küçük tüm çift fibonacci sayılarını yazdırır
import time
fib1=1
fib2=1
t=0
n=int(input("Hangi sayıdan küçük tüm çift fibonacci sayılarının toplamını istersiniz?\n"))
time.sleep(0.2)
while(True):
    fib=fib1+fib2
    if int(fib/2)*2==int(fib):
        """
        print("Çift sayı",fib)
        çift sayıları bastırmak isterseniz
        """
        t=t+fib

    if fib>n:
        print("\n",n,"sayısından küçük tüm çift fibonacci sayılarının toplamı:",t)
        break
    else:
        fib1=fib2
        fib2=fib
input("\n Çıkmak için enter'a basın...")
