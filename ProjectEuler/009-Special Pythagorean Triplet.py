#Özel pisagor üçgeni (a + b + c = 1000 ve a^2 + b^2 = c^2)
a=0
b=1
c=(a**2+b**2)**0.5
while(True):
    if a != 334:
        a += 1
    else:
        b += 1
        a = 1
    if type((a**2)+(b**2)) == int:
        c = (a**2+b**2) ** 0.5
        if a + b + c == 1000:
            print("a: {}\nb: {}\nc: {}".format(a,b,int(c)))
            break
    else:
        a += 1    
input()
