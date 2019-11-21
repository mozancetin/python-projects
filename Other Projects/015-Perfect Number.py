#Girilen sayının mükemmel sayı olup olmadığını kontrol eder.
n = int(input("Sayı girin: "))
toplam = 0
for i in range(1,(n//2)+1):
    if n%i==0:
        toplam += i
if toplam==n:
    print("Bu bir mükemmel sayı!")
else:
    print("Bu bir mükemmel sayı değil!")
        
input()
