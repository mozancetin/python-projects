def collatz(n):
    chain = 1
    while(n!=1):
        if n % 2 == 0:
            n = n / 2
            chain += 1
        else:
            n = 3 * n + 1
            chain += 1
    return chain

lc = 0 #longest chain
sn = 1000000 #starting number
for n in range(1000000,1,-1):
    zincir_sayısı = collatz(n)
    if lc < zincir_sayısı:
        lc = zincir_sayısı
        sn = n
print("Starting Number:",sn,"\n"+"Longest Chain:",lc)

    
