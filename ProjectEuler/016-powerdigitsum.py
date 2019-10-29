#2^1000 sayısının basamakları toplamı
n = 2**1000
toplam = 0
while(n>=10):
    toplam += n % 10
    n = n // 10
toplam += n
print("2^1000 sayısının basamakları toplamı: {}".format(toplam))
input()
