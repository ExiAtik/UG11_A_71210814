#Yoan Adhitama
#UG11_A_71210814

def hitung_hapus() :
    a = input("Masukan Kalimat : ")
    b = int(input("Index Start : ")) + 1
    c = int(input("Index Stop : ")) + 1

    dihapus = c - b + 1 
    hasil = (dihapus/len(a)) * 100

    if b > len(a) or c > len(a) : 
        return 0.0
    elif hasil < 0 :
        return 0.0
    else : 
        return hasil

print(hitung_hapus())
 