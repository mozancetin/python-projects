from fonksiyon import bs
n = int(input("Bir sayı girin: "))
toplam = 0
us = bs(n)
m = n
for i in range(1,bs(n)+1):
    toplam += (n - (int(n/10)*10))**us
    n = int(n/10)
if toplam == m:
    print("Armstrong sayısı!")
else:
    print("Armstrong sayısı değil!")
input()
