# Fungsi untuk menghitung luas persegi
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

# Fungsi untuk menghitung luas lingkaran
def hitung_luas_lingkaran(jari_jari):
  """
  Fungsi untuk menghitung luas lingkaran.

  Args:
    jari_jari: Jari-jari lingkaran.

  Returns:
    Luas lingkaran.
  """
  import math
  luas = math.pi * jari_jari * jari_jari
  return luas

# Fungsi untuk menghitung luas segitiga
def hitung_luas_segitiga(alas, tinggi):
  """
  Fungsi untuk menghitung luas segitiga.

  Args:
    alas: Panjang alas segitiga.
    tinggi: Tinggi segitiga.

  Returns:
    Luas segitiga.
  """
  luas = 0.5 * alas * tinggi
  return luas

# Contoh penggunaan
# Luas persegi
print('')
panjang_sisi_persegi = 5
luas_persegi = hitung_luas_persegi(panjang_sisi_persegi)
print(f"Luas persegi dengan sisi {panjang_sisi_persegi} adalah: {luas_persegi}")

# Luas lingkaran
print('')
jari_jari_lingkaran = 3
luas_lingkaran = hitung_luas_lingkaran(jari_jari_lingkaran)
print(f"Luas lingkaran dengan jari-jari {jari_jari_lingkaran} adalah: {luas_lingkaran:.2f}")

# Luas segitiga
print('')
alas_segitiga = 4
tinggi_segitiga = 6
luas_segitiga = hitung_luas_segitiga(alas_segitiga, tinggi_segitiga)
print(f"Luas segitiga dengan alas {alas_segitiga} dan tinggi {tinggi_segitiga} adalah: {luas_segitiga}")