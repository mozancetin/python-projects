a = int(input("İkinci dereceden terimin katsayısı: "))
b = int(input("Birinci dereceden terimin katsayısı: "))
c = int(input("Sabit terim: "))
delta = b**2-4*a*c


if delta<0:
    print("Reel kök yok.")
    
elif delta==0:
    x = -b/(2*a)
    print("Çakışık kök:",x)
    
        
else:
    x1= (-b-delta**0.5)/(2*a)
    x2= (-b+delta**0.5)/(2*a)
    print("Kökler: ",x1,x2)
input()
