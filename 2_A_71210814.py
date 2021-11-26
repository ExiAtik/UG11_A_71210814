#Yoan Adhitama
#UG11_A_71210814

def ambil_tengah(huruf, penjumlahan = 0) :
    if(penjumlahan) :
        tambah = len(huruf)
        bagi = (tambah // 2)
        return(huruf[bagi + penjumlahan])

    else :
        tambah = len(huruf)
        bagi = (tambah // 2)
        return(huruf[bagi])

print(ambil_tengah("abcdefg", 1))
print(ambil_tengah("abcdefg", 2))
print(ambil_tengah("abcd"))
