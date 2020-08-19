def cifttek(n):
    #bir sayının tek mi çift mi olduğunu geri döndüren fonksiyon
    if n%2 == 0:
        return(1)
    else:
        return(0)



def fibonacci(n):
    #n. fibonacci sayısını bastıran fonksiyon
    fib1 = 1
    fib2 = 1
    for i in range(3,n+1):
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
    print(fib)



def faktoriyel(n):
    #n! sayısını bastıran fonksiyon
    carpim = 1
    for i in range(1,n+1):
        carpim *= i
    print(carpim)



def toplam(n):
    #n'e kadar olan sayıların toplamını bastıran fonksiyon
    toplam = 0
    for i in range(1,n+1):
        toplam += i
    print(toplam)



def asal(n):
    #n sayısının asal olup olmadığını geri döndüren fonksiyon
    i=2
    while(True):
        if n==0 or n==1:
            return(0)
            break
        else:
            if n<i**2 :
                return(1)
                break
            if int(n/i)*i==n :
                return(0)
                break
            else:
                if int(i/2)*2==i :
                    i=i+1
                else:
                    i=i+2



def loadscreen(s):
    #Basit bir yükleme ekranı
    import time
    for i in range(101):
        print(50*"\n")
        print("Yükleniyor % {}...".format(i))
        time.sleep(s)
    print("Yükleme Tamamlandı...")


def triangle(n):
    #n. üçgensel sayıyı bulan fonksiyon
    sayi = n*(n+1)//2
    return(sayi)

def bolenler(n):
    #bir sayının bölenlerinin sayısını geri döndüren fonksiyon
    c = 0
    for i in range(1,(n//2)+1):
        if n%i == 0:
            c += 1
    return(c+1)
    
def bs(n):
    #bir sayının kaç basamaklı olduğunu geri döndüren fonksiyon
    bs = 0
    while(int(n/10)!=0):
        n = int(n/10)
        bs += 1
    return(bs+1)
def bt(n):
    #bir sayının basamaklarındaki sayıların toplamını bulan fonksiyon
    bt = 0
    while(True):
        bt = bt + (n - int(n/10)*10)
        if (n>0):
            n = int(n/10)
        else:
            return(bt)
def ayna(sayi):
    if int(str(sayi)[::-1]) == sayi:
        return True
    else:
        return False
