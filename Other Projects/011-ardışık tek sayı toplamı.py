#Ardışık tek sayıların toplamını bulan program
n = int(input("Kaç tane ardışık tek sayı toplansın: "))
for i in range(1,2*n+1,2):
    print(i)
print("\n{}. adıma kadar olam tüm tek sayıların toplamı: {}".format(n,n**2))
input()
