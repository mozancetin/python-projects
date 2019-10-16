"""
10 kapı var ve bu kapıların birinde hediye var. Hangi kapıda hediye olduğunu tahmin et!
8 boş kapı açılacak ve sana hangi kapıyı istediğin tekrar sorulacak. Bakalım hediyeyi bulabilecek misin?
"""
import random

tercih=int(input("Tercihinizi girin:"))
odul= random.randint(1,10)
if tercih!=odul:
    print("Kalan kapılar:",tercih,"ve",odul)
    skarar= int(input("Hangi numaralı kapıyı seçmek istersiniz? \n"))
    if odul==skarar:
        print("Kazandınız")
    else:
        print("Kaybettiniz")
else:
    while True:
        tercih=random.randint(1,10)
        if tercih!=odul:
            break
    print("Kalan kapılar:",tercih,"ve",odul)
    skarar=int(input("Hangi numaralı kapıyı seçmek istersiniz? \n"))
    if odul==skarar:
        print("Kazandınız")
    else:
        print("Kaybettiniz")
input()
