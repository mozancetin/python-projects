#100 sayının toplamının karesi ile karelerinin toplamı arasındaki fark
tk = (100*101//2)**2 #toplamlarının karesi
kt=0 #karelerinin toplamı
i=1
while(i<=100):
    kt += i**2
    i+=1
fark = tk-kt
print("100 sayının toplamının karesi ile karelerinin toplamı arasındaki fark:",fark)
input()
