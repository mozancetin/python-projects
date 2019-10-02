import random
tercih=int(input("Tercihinizi girin:"))
odul=random.randint(1,10)
if tercih!=odul :
    print("Tercihiniz:",tercih, "Kalan kapı:",odul)
    skarar=int(input("Hangi numaralı kapıyı seçmek istersiniz? \n")
    if odul==skarar:
        print("Kazandınız")
    else:
        print("Kaybettiniz")
else:
    while(True):
        tercih=random.randint(1,10)
        if tercih!=odul:
            break
    print("Tercihiniz:",tercih, "Kalan kapı:",odul)
    skarar=int(input("Hangi numaralı kapıyı seçmek istersiniz? \n")
    if odul==skarar:
        print("Kazandınız")
    else:
        print("Kaybettiniz")
input()
