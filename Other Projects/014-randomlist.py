import random
liste = []
c = 0
while(True):
    print(50*"\n")
    n =input("Listeye ne eklensin? ")
    liste.append(n)
    print(50*"\n")
    for i in range(len(liste)):
        print("""-------------------------------
{}. Seçeneğiniz: {}
-------------------------------""".format(i+1,liste[i]))
    c = int(input("\n\nBaşka bir şey daha eklemek için 1 bitirmek için 2 ye basın.\n"))
    if c!= 1:
        break
print(50*"\n")
print("Kazanan Seçenek: {}".format(random.choices(liste)))

input()
    
