liste = []
a = int(input("Kaç sayı gireceksiniz?\n"))

while (len(liste) < a):
    n = int(input("Sayı girin:"))
    liste.append(n)
    print(liste)

liste.sort()
print(liste)

#ÇİFT İSE:

if a % 2 == 0:
    i=0
    ortanca = (liste[int(a / 2) - 1] + liste[int(a / 2)]) / 2
    print("Ortanca(Medyan):",ortanca)

    
    ebs = 1
    while(i<=a):       
        b=liste.count(i)  
        if b>ebs:
            dm=1
            ebs=b
            mod = i
            i+=1
        elif b==ebs:
            dm=0
            i+=1
        else:
            dm = 0
            i+=1
    if dm==0:
        mod = "Mod yok"
            
    print("Tepe Değeri(Mod):",mod)
    i=0
    
    toplam=0
    while(i<=a-1):
        toplam = toplam + liste[i]
        i+=1
    ao = toplam/a
    print("Aritmetik Ortalama:",ao)

    aciklik = liste[a-1] - liste[0]
    print("Açıklık:",aciklik)










#TEK İSE:
    
else:
    i=0
    ortanca = liste[int((a-1)/2)]
    print("Ortanca(Medyan):",ortanca)
    ebs = 1
    while(i<=a):
        b=liste.count(i)  
        if b>ebs:
            dm=1
            ebs=b
            mod = i
            i+=1
        elif b==ebs:
            dm=0
            i+=1
        else:
            dm = 0
            i+=1
    if dm==0:
        mod = "Mod yok"
            
    print("Tepe Değeri(Mod):",mod)
    i=0
    
    toplam=0
    while(i<=a-1):
        toplam = toplam + liste[i]
        i+=1
    ao = toplam/a
    print("Aritmetik Ortalama:",ao)

    aciklik = liste[a-1] - liste[0]
    print("Açıklık:",aciklik)


    
"""
    ceyrekacik = liste[int((a+1)/2)] - liste[]


#çeyrekler açıklığı eklenecek

1,2,3,4,5,6,7,8

"""



input()


