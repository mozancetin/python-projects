import time
import random
rcan=10
can=10
t=1
while(True):
    print("\n"*50)
    attack=random.randint(1,5)
    rattack=random.randint(1,5)
    
    if (t%2) == 1:
        if attack==1:
            print("Saldırı yapılıyor...")
            time.sleep(1)
            print("Weak!",attack)
            rcan=rcan-attack
            if rcan<=0:
                    print("Tebrikler rakip öldü!")
                    break
            print("Rakibin kalan canı:",rcan)
            time.sleep(2)
            t+=1
        elif attack==2:
            print("Saldırı yapılıyor...")
            time.sleep(1)
            print("Normal!",attack)
            rcan=rcan-attack
            if rcan<=0:
                    print("Tebrikler rakip öldü!")
                    break
            print("Rakibin kalan canı:",rcan)
            t+=1
            time.sleep(2)
        elif attack==3:
            print("Saldırı yapılıyor...")
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
            print("Saldırı yapılıyor...")
            time.sleep(1)
            print("Too Strong!",attack)
            rcan=rcan-attack
            if rcan<=0:
                    print("Tebrikler rakip öldü!")
                    break
            print("Rakibin kalan canı:",rcan)
            t+=1
            time.sleep(2)

        
    elif (t%2) == 0:
        if rattack==1:
            print("Rakip saldırı yapıyor...")
            time.sleep(1)
            print("Weak!",rattack)
            can=can-rattack
            if can<=0:
                    print("Mezarı boyladın!")
                    break
            print("Kalan canın:",can)
            t+=1
            time.sleep(2)
        elif rattack==2:
            print("Rakip saldırı yapıyor...")
            time.sleep(1)
            print("Normal!",rattack)
            can=can-rattack
            if can<=0:
                    print("Mezarı boyladın!")
                    break
            print("Kalan canın:",can)
            t+=1
            time.sleep(2)
        elif rattack==3:
            print("Rakip saldırı yapıyor...")
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
            print("Rakip saldırı yapıyor...")
            time.sleep(1)
            print("Too Strong!",rattack)
            can=can-rattack
            if can<=0:
                    print("Mezarı boyladın!")
                    break
            print("Kalan canın:",can)
            t+=1
            time.sleep(2)
            
        
input()
