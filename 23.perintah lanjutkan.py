# Perulangan for dengan continue
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in angka:
  if i % 2 == 0:  # Jika angka genap
    continue  # Lewati ke iterasi berikutnya
  print(f"Angka ganjil: {i}")

# Perulangan while dengan continue
i = 1
while i <= 10:
  if i % 2 == 0:  # Jika angka genap
    i += 1  # Lanjutkan ke iterasi berikutnya tanpa mencetak
    continue
  print(f"Angka ganjil: {i}")
  i += 1