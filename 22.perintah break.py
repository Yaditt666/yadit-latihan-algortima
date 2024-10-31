# Perulangan for dengan break
buah = ["semangka", "pear", "jeruk", "mangga"]

for buah_ini in buah:
  print(buah_ini)
  if buah_ini == "jeruk":
    break

# Perulangan while dengan break
i = 1
while i <= 10:
  print(i)
  if i == 5:
    break
  i += 1