#perintah return pada funtion
def cek_genap(angka):
  """
  Fungsi untuk memeriksa apakah sebuah angka genap.

  Args:
    angka: Angka yang akan diperiksa.

  Returns:
    True jika angka genap, False jika tidak.
  """
  if angka % 2 == 0:
    return True
  else:
    return False

# Memanggil fungsi dan mencetak hasilnya
bilangan = 11
if cek_genap(bilangan):
  print(f"{bilangan} adalah bilangan genap.")
else:
  print(f"{bilangan} adalah bilangan ganjil.")