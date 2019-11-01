soru = int(input("Üçgenin tipini mi yoksa dörtgenin tipini mi bulmak istiyorsunuz? (Üçgen için 1, Dörtgen için 2 yazın)\n"))

if soru == 1:
    print(50*"\n")
    print("Üçgen seçtiniz...")
    k1=int(input("Birinci kenar uzunluğu: "))
    k2=int(input("İkinci kenar uzunluğu: "))
    k3=int(input("Üçüncü kenar uzunluğu: "))
    if abs(k1-k2)<k3<abs(k1+k2):
        if k1 == k2 == k3:
            print("Eşkenar üçgen belirtir")
        elif k1 == k2 or k1 == k3:
            print("İkiz üçgen belirtir")
        else:
            print("Çeşitkenar üçgen belirtir")

    elif abs(k1-k3)<k2<abs(k1+k3):
        if k1 == k2 == k3:
            print("Eşkenar üçgen belirtir")
        elif k1 == k2 or k1 == k3:
            print("İkiz üçgen belirtir")
        else:
            print("Çeşitkenar üçgen belirtir")

    elif abs(k3-k2)<k1<abs(k3+k2):
        if k1 == k2 == k3:
            print("Eşkenar üçgen belirtir")
        elif k1 == k2 or k1 == k3:
            print("İkiz üçgen belirtir")
        else:
            print("Çeşitkenar üçgen belirtir")

    else:
        print("Üçgen belirtmez")

elif soru == 2:
    print(50*"\n")
    print("Dörtgen seçtiniz...\n")
    k1=int(input("Birinci kenar uzunluğu: "))
    k2=int(input("İkinci kenar uzunluğu: "))
    k3=int(input("Üçüncü kenar uzunluğu: "))
    k4=int(input("Dördüncü kenar uzunluğu: "))
    if k1 == k2 == k3 == k4:
        print("\nKare")
    elif (k1 == k3 and k2 == k4) or (k1 == k2 and k3 == k4) or (k1 == k4 and k2 == k3):
        print("\nDikdörtgen")
    else:
        print("\nSıradan bir dörtgen")

input()
    
    
