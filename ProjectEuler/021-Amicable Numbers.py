def amicable(n):
    toplam = 1
    q = int(n**(1/2)//1)
    for p in range(2,q+1):
        if (n%p==0):
            toplam += p + n/p
    if (q**2==n):
        toplam = toplam - q
    return(int(toplam))

gtoplam = 0
for m in range(2,10000):
    s = amicable(m)
    if m == s:
        continue
    if m == amicable(s) and s<10000:
        gtoplam += m
        print("Amicable Number: {} and {}".format(m,s))
print("Amicable Sum: {}".format(gtoplam))
input()
