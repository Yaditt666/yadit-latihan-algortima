#named parameter/argumen kata kunci
def make_profile(nama, umur, kota="Tidak Diketahui"):
    print(f"Nama: {nama}")
    print(f"Umur: {umur}")
    print(f"Kota: {kota}")

# Memanggil fungsi dengan urutan parameter yang benar
make_profile("yadit", 18)  

print('')

# Memanggil fungsi menggunakan keyword arguments (argumen kata kunci)
make_profile(umur=18, nama="elvy", kota="majene")

print('')

# Memanggil fungsi dengan keyword argument sebagian
make_profile("isda",18, kota="majene")

