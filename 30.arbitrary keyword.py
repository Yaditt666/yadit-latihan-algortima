#argumen kata kunci arbitrer ( **kwargs)
def cetak_info(**info):
    for kunci, nilai in info.items():
        print(f"{kunci}: {nilai}")

# Memanggil fungsi dengan sejumlah pasangan key-value
cetak_info(nama="yadit", umur=18, kota="majene")

print('')

def buat_profil(**data):
    print("Profil Pengguna:")
    for kunci, nilai in data.items():
        print(f"{kunci.capitalize()}: {nilai}")

# Memanggil fungsi dengan berbagai argumen kata kunci
buat_profil(nama="Elvy", umur=18, pekerjaan="Sofware development", kota="majene",)
