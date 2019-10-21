#2 milyondan küçük tüm asal sayıların toplamı
n=3
i=3
toplam=0
print("Bu işlem biraz uzun sürebilir... (yaklaşık 3 dakika)")
while(n<=2000000):
    if n<i**2 :
        toplam += n
        n += 2
        i = 2
    if int(n/i)*i==n :
        n += 2
        i = 2
    else:
        if int(i/2)*2==i :
            i=i+1
        else:
            i=i+2
print("Toplam:",toplam+2)
input()
