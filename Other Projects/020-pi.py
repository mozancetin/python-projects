#pi sayısını hesaplayan program Gregory–Leibniz yöntemi
maxn = int(input("Hassasiyet: "))
n = 0
pi = 0
while(n<maxn):
    pi += 4*(((-1) ** n) / (2*n + 1))
    n += 1
print(pi)

    
