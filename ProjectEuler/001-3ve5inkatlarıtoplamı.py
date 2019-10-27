#1000'den küçük 3 ve 5'in katlarının toplamını yazdıran program
toplam=0
i=1
while(i<1000):
    if i%3==0:
        toplam+=i
    elif i%5==0:
        toplam+=i
    i+=1
print(toplam)
input()
