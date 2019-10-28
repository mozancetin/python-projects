#Ardışık çift sayıların toplamını bulan program
n = int(input("Kaç tane ardışık tek sayı toplansın: "))
for i in range(2,2*n+1,2):
    print(i)
print("\n{}. adıma kadar olam tüm çift sayıların toplamı: {}".format(n,n*(n+1)))
input()
