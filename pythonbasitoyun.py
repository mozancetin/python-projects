import random
import time

"""
balik,tost,simit,cay,para,kılıç,kalkan,zırh(can)
"""
canta = [0, 0, 0, 0,30,1,1,1]
can = 100
aclik = 100
print("Game version: Alpha 0.0.0.5\nOyunu denemen için sana 30 TL verdim. İyi eğlenceler")
nick = input("Sana nasıl seslenmeliyim: ")
print("Merhaba", nick, "Oyunuma Hoşgeldin!\n")
while (True):
    print("\n" * 50)
    print("Burada yapabileceğin birkaç şeyi görüyorsun...")
    action = int(input(
        """
**************************************************
Bir eylem gerçekleştirmek için numarasını yaz... \n\n 1 | Market\n 2 | Mini games\n 3 | Çantana bak\n 4 | Savaşa gir.(Kazanırsan +20 tl) \n\n
**************************************************
"""))
    if action == 1:
        print("\n" * 50)
        print("Markete hoşgeldin!\n")
        action = int(input(
            " 1 | Balık....6TL\n 2 | Tost.....4TL \n 3 | Simit....2TL \n 4 | Çay......1TL  \n\nAlmak istediğin şeyin numarasını gir: "))
        if action == 1:

            if canta[4] >= 6:
                canta[4] = canta[4] - 6
                print("Balık aldın! Kalan paran: ", canta[4],"TL")
                canta[0] += 1
                input("Devam etmek için enter tuşuna bas\n ")
            else:
                print("\nYeterince paran yok gibi görünüyor...")
                input("Devam etmek için enter tuşuna bas\n ")


        elif action == 2:

            if canta[4] >= 4:
                canta[4] = canta[4] - 4
                print("Tost aldın! Kalan paran: ", canta[4],"TL")
                canta[1] += 1
                input("Devam etmek için enter tuşuna bas\n ")
            else:
                print("\nYeterince paran yok gibi görünüyor...")
                input("Devam etmek için enter tuşuna bas\n ")



        elif action == 3:

            if canta[4] >= 1:
                canta[4] = canta[4] - 2
                print("Simit aldın! Kalan paran: ", canta[4],"TL")
                canta[2] += 1
                input("Devam etmek için enter tuşuna bas\n ")
            else:
                print("\nYeterince paran yok gibi görünüyor...")
                input("Devam etmek için enter tuşuna bas\n ")


        elif action == 4:

            if canta[4] >= 1:
                canta[4] = canta[4] - 1
                print("Çay aldın! Kalan paran: ", canta[4],"TL")
                canta[3] += 1
                input("Devam etmek için enter tuşuna bas\n ")
            else:
                print("\nYeterince paran yok gibi görünüyor...")
                input("Devam etmek için enter tuşuna bas\n ")




    elif action == 2:
        print("\n" * 50)
        print("Burada oynayabileceğin şans oyunlarını görüyorsun")
        action = int(input("Oynamak için numarasını yaz... \n\n 1 | Zar oyunu 5TL\n 2 | 21 Oyunu 10TL\n\n "))
        if action == 1:
            if canta[4] >= 5:
                canta[4] = canta[4] - 5
                print("\n" * 50)
                print("Zar oyununu seçtin.\nKalan Paran: ", canta[4],
                      "TL\nŞimdi sana nasıl oynaman gerektiğini anlatayım...\n"
                      "Bir zar atılacak ve sonraki zar o sayıdan büyük mü küçük mü gelecek tahmin et!\nTahminin doğru çıkarsa para kazanacaksın...")
                action = int(input("\n\n 1 Zarla oynamak istersen: 1 \n 2 Zarla oynamak istersen: 2 \n\n "))

                while (True):
                    if action == 1:
                        print("\n" * 50)
                        zar1 = random.randint(1, 6)
                        print("Zar", zar1, "çıktı")
                        action = int(input("Sence sonraki daha mı büyük yoksa daha mı küçük olacak?\n\n Daha büyük çıkacak diyorsan: 1\n Daha küçük çıkacak diyorsan: -1\n "))
                        zar2 = random.randint(1, 6)
                        if action == 1:
                            if zar1 < zar2:
                                print("\n" * 50)
                                canta[4] = canta[4] + 10
                                print("Doğru bildin. 10TL hesabına aktarıldı. Yeni bakiyen:",canta[4],"TL")
                                again = int(input("Bir daha oynamak ister misin?(5TL)\n\n Evet için: 1\n Hayır için: 2\n\n "))
                                if again == 1:
                                    if canta[4] >= 5:
                                        print("\n" * 50)
                                        canta[4] = canta[4] - 5
                                        print(" Oyun tekrar başlatıldı...\n\n")
                                    else:
                                        print("\n" * 50)
                                        print("\nYeterince paran yok gibi görünüyor...")
                                        input("Devam etmek için enter tuşuna bas\n ")
                                        break
                                elif again == 2:
                                    print("Oynadığın için teşekkürler")
                                    break

                            else:
                                print("\n" * 50)
                                print("Yanlış bildin. Bakiyen: ",canta[4],"TL")
                                again = int(input("Bir daha oynamak ister misin?(5TL)\n\n Evet için: 1\n Hayır için: 2\n\n"))
                                if again == 1:
                                    if canta[4] >= 5:
                                        print("\n" * 50)
                                        canta[4] = canta[4] - 5
                                        print(" Oyun tekrar başlatıldı...\n\n")
                                    else:
                                        print("\n" * 50)
                                        print("\nYeterince paran yok gibi görünüyor...")
                                        input("Devam etmek için enter tuşuna bas\n ")
                                        break
                                elif again == 2:
                                    print("Oynadığın için teşekkürler")
                                    break



                        elif action == -1:
                            if zar1 > zar2:
                                canta[4] = canta[4] + 10
                                print("\n" * 50)
                                print("Doğru bildin. 10TL hesabına aktarıldı. Yeni bakiyen:",canta[4],"TL")
                                again = int(input("Bir daha oynamak ister misin?(5TL)\n\n Evet için: 1\n Hayır için: 2\n "))
                                if again == 1:
                                    if canta[4] >= 5:
                                            print("\n" * 50)
                                            canta[4] = canta[4] - 5
                                            print(" Oyun tekrar başlatıldı...\n\n")
                                    else:
                                            print("\n" * 50)
                                            print("\nYeterince paran yok gibi görünüyor...")
                                            input("Devam etmek için enter tuşuna bas\n ")
                                            break
                                elif again == 2:
                                    print("Oynadığın için teşekkürler")
                                    break

                            else:
                                print("\n" * 50)
                                print("Yanlış bildin. Bakiyen: ",canta[4],"TL")
                                again = int(input("Bir daha oynamak ister misin?(5TL)\n\n Evet için: 1\n Hayır için: 2\n "))
                                if again == 1:
                                    if canta[4] >= 5:
                                        print("\n" * 50)
                                        canta[4] = canta[4] - 5
                                        print(" Oyun tekrar başlatıldı...\n\n")
                                    else:
                                        print("\n" * 50)
                                        print("\nYeterince paran yok gibi görünüyor...")
                                        input("Devam etmek için enter tuşuna bas\n ")
                                        break
                                elif again == 2:
                                    print("Oynadığın için teşekkürler")
                                    break
                    elif action == 2:
                        print("\n" * 50)
                        zar1 = random.randint(1, 6)
                        print("Zar", zar1, "çıktı")
                        action = int(input(
                            "Sence sonraki daha mı büyük yoksa daha mı küçük olacak?\n\n Daha büyük çıkacak diyorsan: 1\n Daha küçük çıkacak diyorsan: -1\n "))
                        zar2 = random.randint(1, 6)
                        if action == 1:
                            if zar1 < zar2:
                                canta[4] = canta[4] + 10
                                print("\n" * 50)
                                print("Doğru bildin. 10TL hesabına aktarıldı. Yeni bakiyen:",canta[4],"TL")
                                again = int(input("Bir daha oynamak ister misin?(5TL)\n\n Evet için: 1\n Hayır için: 2\n "))
                                if again == 1:
                                    if canta[4] >= 5:
                                        print("\n" * 50)
                                        canta[4] = canta[4] - 5
                                        print(" Oyun tekrar başlatıldı...\n\n")
                                    else:
                                        print("\n" * 50)
                                        print("\nYeterince paran yok gibi görünüyor...")
                                        input("Devam etmek için enter tuşuna bas\n ")
                                        break
                                elif again == 2:
                                    print("Oynadığın için teşekkürler")
                                    break

                            else:
                                print("\n" * 50)
                                print("Yanlış bildin. Bakiyen: ",canta[4],"TL")
                                again = int(input("Bir daha oynamak ister misin?(5TL)\n\n Evet için: 1\n Hayır için: 2\n "))
                                if again == 1:
                                    if canta[4] >= 5:
                                        print("\n" * 50)
                                        canta[4] = canta[4] - 5
                                        print(" Oyun tekrar başlatıldı...\n\n")
                                    else:
                                        print("\n" * 50)
                                        print("\nYeterince paran yok gibi görünüyor...")
                                        input("Devam etmek için enter tuşuna bas\n ")
                                        break
                                elif again == 2:
                                    print("Oynadığın için teşekkürler")
                                    break



                        elif action == -1:
                            if zar1 > zar2:
                                canta[4] = canta[4] + 10
                                print("\n" * 50)
                                print("Doğru bildin. 10TL hesabına aktarıldı. Yeni bakiyen:",canta[4],"TL")
                                again = int(input("Bir daha oynamak ister misin?(5TL)\n\n Evet için: 1\n Hayır için: 2\n "))
                                if again == 1:
                                    if canta[4] >= 5:
                                        print("\n" * 50)
                                        canta[4] = canta[4] - 5
                                        print(" Oyun tekrar başlatıldı...\n\n")
                                    else:
                                        print("\n" * 50)
                                        print("\nYeterince paran yok gibi görünüyor...")
                                        input("Devam etmek için enter tuşuna bas\n ")
                                        break
                                elif again == 2:
                                    print("Oynadığın için teşekkürler")
                                    break

                            else:
                                print("\n" * 50)
                                print("Yanlış bildin. Bakiyen:",canta[4],"TL")
                                again = int(input("Bir daha oynamak ister misin?(5TL)\n\n Evet için: 1\n Hayır için: 2\n "))
                                if again == 1:
                                    if canta[4] >= 5:
                                        print("\n" * 50)
                                        canta[4] = canta[4] - 5
                                        print(" Oyun tekrar başlatıldı...\n\n")
                                    else:
                                        print("\n" * 50)
                                        print("\nYeterince paran yok gibi görünüyor...")
                                        input("Devam etmek için enter tuşuna bas\n ")
                                        break
                                elif again == 2:
                                    print("Oynadığın için teşekkürler")
                                    break



            else:
                print("\nYeterince paran yok gibi görünüyor")
                input("Devam etmek için enter tuşuna bas\n")









        if action==2:
                    if canta[4] >= 10:
                        canta[4] = canta[4] - 10
                        print("\n"*50)
                        print("21 Oyununu seçtin.\nKalan paran: ",canta[4],"TL\n --Şimdi sana nasıl oynaman gerektiğini anlatayım...\n --Rastgele 2 kart seçilecek sonra kartlar tek tek alınacak.\n --İstediğin zaman duracaksın ve toplamlar açılacak.\n --Eğer kartlar açıldığında 21 sayısına rakinbinden \n-daha fazla yaklaşırsan kazanırsın.\n --Toplamlardan 1'i 21 olduğu an oyun biter.")
                        action=int(input("\nBaşlamak için 1  yaz\n"))
                        if action==1:
                            print("\n"*50)
                            toplam1=0
                            toplam2=0
                            kart1=random.randint(1,10)
                            kart2=random.randint(1,10)
                            kart3=random.randint(1,10)
                            kart4=random.randint(1,10)
                        while(True):
                            print("\n"*50)
                            toplam1=kart1+kart2+toplam1
                            toplam2=kart3+kart4+toplam2
                            if toplam1>=21 and toplam2>=21:
                                print("Toplamlarınız eşit! Berabere kaldınız... (Oyun parası hesabınıza iade edildi)\n")
                                canta[4] = canta[4] + 10
                                print("Bakiyen:",canta[4],"\n")
                                input("Devam etmek için enter'a bas")
                                break
                            
                            elif toplam2>=21:
                                print("Çektiğin kartlar:",kart3,"ve",kart4,"\nToplamın:",toplam2,"\nRakibinin toplamı:",toplam1,"\nToplam 21'e eşit veya büyük olduğundan dolayı oyunu kaybettin...")
                                print("Bakiyen:",canta[4],"\n")
                                input("Devam etmek için enter'a basın")
                                break
                            
                            elif toplam1>=21:
                                print("Rakibinin toplamı 21'e eşit veya büyük olduğundan \n-dolayı oyunu sen kazandın!(Ödülün 20TL)\n")
                                print("Rakibinin toplamı:",toplam1,"\nSenin toplamın:",toplam2)
                                canta[4] = canta[4] + 20
                                print("Yeni bakiyen:",canta[4],"TL")
                                input("Devam etmek için enter'a bas...")
                                break
                                                            
                            else:
                                print("Çektiğiniz kartlar:",kart3,"ve",kart4,"\nToplam:",toplam2)
                                action=int(input("Bir kart daha çekmek için 1'e , durmak ve toplamları açmak için 2'ye basın.\n\n"))
                                if action==1:
                                    kart3=random.randint(1,10)
                                    kart4=0
                                    kart1=random.randint(1,10)
                                    kart2=0
                                elif action==2:
                                    print("\n"*50)
                                    print(" Senin toplamın:",toplam2,"\n Rakibinin toplamı:",toplam1)
                                    if toplam2>toplam1:
                                        print("21'e rakibinden daha yakınsın, sen kazandın!(Ödülün 20 TL)\n")
                                        canta[4] = canta[4] + 20
                                        print("Yeni bakiyen:",canta[4],"TL")
                                        input("Devam etmek için enter'a bas")
                                        break
                                    elif toplam2<toplam1:
                                        print("Rakibin 21'e daha yakın. Üzgünüm kaybettin...")
                                        print("Bakiyen:",canta[4],"\n")
                                        input("Devam etmek için enter'a bas...")
                                        break
                                    elif toplam1==toplam2:
                                        print("Toplamlarınız eşit! Berabere kaldınız... (Oyun parası hesabınıza iade edildi)\n")
                                        canta[4] = canta[4] + 10
                                        print("Bakiyen:",canta[4],"\n")
                                        input("Devam etmek için enter'a bas")
                                        break
                               
                    else:
                        print("\nYeterince paran yok gibi görünüyor")
                        input("Devam etmek için enter tuşuna bas\n")








    elif action == 3:
        print("\n" * 50)
        print("Çantanızda: \n\n {} adet balık\n {} adet tost\n {} adet simit\n {} bardak çay\n {} seviye kılıç\n {} seviye kalkan\n {} seviye zırh\n\nbulunmaktadır...\n\nParanız: {} TL".format(canta[0],canta[1],canta[2],canta[3],canta[5],canta[6],canta[7],canta[4]))
        input("\nDevam etmek için enter tuşuna bas\n")
        





    elif action == 4:

        rcan=100
        t=1
        #item0=canta5   item1=canta6   item2=canta7

        a=10
        b=50

        c=10
        d=50

        if canta[5]==1:
            a=30
            b=70
        if canta[7]==1:
            can=can+20


        while(True):
            print("\n"*50)
            attack=random.randint(a,b)
            rattack=random.randint(c,d)
            if canta[6]==1:
                rattack=rattack-1
    
            if (t%2) == 1:
                if attack<=10:
                    print("[ Tur {} ] Saldırı yapılıyor...".format(t))
                    time.sleep(1)
                    print("Weak!",attack)
                    rcan=rcan-attack
                    if rcan<=0:
                            print("Tebrikler rakip öldü!")
                            break
                    print("Rakibin kalan canı:",rcan)
                    time.sleep(2)
                    t+=1
                elif 10 < attack <= 20:
                    print("[ Tur {} ] Saldırı yapılıyor...".format(t))
                    time.sleep(1)
                    print("Normal!",attack)
                    rcan=rcan-attack
                    if rcan<=0:
                            print("Tebrikler rakip öldü!")
                            break
                    print("Rakibin kalan canı:",rcan)
                    t+=1
                    time.sleep(2)
                elif 20 < attack <= 30:
                    print("[ Tur {} ] Saldırı yapılıyor...".format(t))
                    time.sleep(1)
                    print("Strong!",attack)
                    rcan=rcan-attack
                    if rcan<=0:
                            print("Tebrikler rakip öldü!")
                            break
                    print("Rakibin kalan canı:",rcan)
                    t+=1
                    time.sleep(2)
                else:
                    print("[ Tur {} ] Saldırı yapılıyor...".format(t))
                    time.sleep(1)
                    print("Too Strong!",attack)
                    rcan=rcan-attack
                    if rcan<=0:
                            print("Tebrikler rakip öldü! (20 Tl hesabına eklendi.)")
                            canta[4] += 20
                            break
                    print("Rakibin kalan canı:",rcan)
                    t+=1
                    time.sleep(2)

        
            elif (t%2) == 0:
                if rattack<=10:
                    print("[ Tur {} ] Rakip saldırı yapıyor...".format(t))
                    time.sleep(1)
                    print("Weak!",rattack)
                    can=can-rattack
                    if can<=0:
                            print("Mezarı boyladın!")
                            break
                    print("Kalan canın:",can)
                    t+=1
                    time.sleep(2)
                elif 10 < rattack <= 20:
                    print("[ Tur {} ] Rakip saldırı yapıyor...".format(t))
                    time.sleep(1)
                    print("Normal!",rattack)
                    can=can-rattack
                    if can<=0:
                            print("Mezarı boyladın!")
                            break
                    print("Kalan canın:",can)
                    t+=1
                    time.sleep(2)
                elif 20 < rattack <= 30:
                    print("[ Tur {} ] Rakip saldırı yapıyor...".format(t))
                    time.sleep(1)
                    print("Strong!",rattack)
                    can=can-rattack
                    if can<=0:
                            print("Mezarı boyladın!")
                            break
                    print("Kalan canın:",can)
                    t+=1
                    time.sleep(2)
                else:
                    print("[ Tur {} ] Rakip saldırı yapıyor...".format(t))
                    time.sleep(1)
                    print("Too Strong!",rattack)
                    can=can-rattack
                    if can<=0:
                            print("Mezarı boyladın!")
                            break
                    print("Kalan canın:",can)
                    t+=1
                    time.sleep(2)
                    
        input("Devam etmek için enter...")

        

input()
