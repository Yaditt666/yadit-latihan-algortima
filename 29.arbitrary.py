#Argumen Posisional Sembarangan ( *args)
def hitung_total(*angka):
    total = 0
    for n in angka:
        total += n
    print("Total:", total)

# Memanggil fungsi dengan jumlah argumen variabel
hitung_total(10, 20, 30) 
hitung_total(5, 10, 15, 20) 
