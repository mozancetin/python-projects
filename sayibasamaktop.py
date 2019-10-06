try:
    n=int(input("Sayıyı girin: "))
    t=int(0)
    while(True):
        t=t+n-int(n/10)*10
        if(n>0):
            n=int(n/10)
        else:
            print("Toplam:",t)
            break
except ValueError:
    print("\033[1;31;40m\nHATA!:Lütfen harf yerine sayı girin \033[0m")
input()
