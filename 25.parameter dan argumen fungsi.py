def hitung_luas_persegi(sisi):
  """
  Fungsi untuk menghitung luas persegi.

  Args:
    sisi: Panjang sisi persegi.

  Returns:
    Luas persegi.
  """
  luas = sisi * sisi
  return luas

# Contoh penggunaan
panjang_sisi = 5
luas_persegi = hitung_luas_persegi(panjang_sisi)
print(f"Luas persegi dengan sisi {panjang_sisi} adalah: {luas_persegi}")

# Contoh dengan argumen default
def sapa(nama, pesan="Selamat pagi!"):
  """
  Fungsi untuk menampilkan pesan sapaan.

  Args:
    nama: yadit.
    pesan: Pesan yang ingin ditampilkan (default: "Selamat pagi!").

  Returns:
    None.
  """
  print(f"Halo {nama}, {pesan}")

# Contoh pemanggilan fungsi sapa
sapa("Yadit")  
sapa("Yadit", "Selamat siang!")  