#matris çarpımı
#Requires numpy

print("Matrislerin boyutlarını girin ( A(mxn) , B(nxp) )")

m = int(input("m: "))
n = int(input("n: "))
p = int(input("p: "))

A = []
B = []
C = []

print("\n")
for i in range(0,m):
    A.append([])
    for x in range(0,n):
        sayi = int(input("A[{}x{}] sayısını girin: ".format(i+1,x+1)))
        A[i].append(sayi)

print("\n")
print("A matrisi: ", A)
input("B matrisini girmek için enter'a basın...")
print(3*"\n")
for i in range(0,n):
    B.append([])
    for x in range(0,p):
        sayi = int(input("B[{}x{}] sayısını girin: ".format(i+1,x+1)))
        B[i].append(sayi)

print("\n")
print("A matrisi: ", A)
print("B matrisi: ", B)
print(5*"\n")

def carpma():
    
    import numpy as np

    Q = np.array([A])
    E = np.array([B])
    C = Q.dot(E)
    print(C[0])

carpma()
input()
