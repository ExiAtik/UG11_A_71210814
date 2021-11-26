#Yoan Adhitama
#UG11_A_71210814

def calculator ():
    print ("======== Calculator sederhana ========")

def tambah ():
    print ("1. Pertambahan")

def kurang ():
    print ("2. Pengurangan")

def kali ():
    print ("3. Perkalian")

def bagi ():
    print ("4. Pembagian")

def pangkat ():
    print ("5. Pangkat")


calculator()
tambah()
kurang()
kali()
bagi()
pangkat()


a = int(input("Masukan pilihan : "))

if a == 1 : 
    b = int(input("Masukan bilangan 1 : "))
    c = int(input("Masukan bilangan 2 : "))
    d = b + c
    print("Hasilnya : ", d )
elif a == 2 :
    b = int(input("Masukan bilangan 1 : "))
    c = int(input("Masukan bilangan 2 : "))
    d = b - c
    print("Hasilnya : ", d )
elif a == 3 :
    b = int(input("Masukan bilangan 1 : "))
    c = int(input("Masukan bilangan 2 : "))
    d = b * c
    print("Hasilnya : ", d )
elif a == 4 :
    b = int(input("Masukan bilangan 1 : "))
    c = int(input("Masukan bilangan 2 : "))
    d = b / c
    print("Hasilnya : ", d )
elif a == 5 : 
    b = int(input("Masukan bilangan 1 : "))
    c = int(input("Masukan bilangan 2 : "))
    d = b ** c
    print("Hasilnya : ", d )
else :
    b = int(input("Masukan bilangan 1 : "))
    c = int(input("Masukan bilangan 2 : "))
    print("Hasilnya : Maaf input operasi antara 1-5")
