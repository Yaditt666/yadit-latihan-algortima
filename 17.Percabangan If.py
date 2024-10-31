#if pernyataan
#if digunakan untuk memeriksa apakah suatu kondisi bernilai True
x = 10
if x > 5:
    print("x lebih besar dari 5")

#if else pernyataan
#elsedigunakan jika kondisi iftidak terpenuhi. Blok kode dalam elseakan dijalankan.
print('')
x = 3
if x > 5:
    print("x lebih besar dari 5")
else:
    print("x tidak lebih besar dari 5")

#if elif else pernyataan
#Jika kondisi pertama iftidak terpenuhi, maka elifakan diperiksa. Jika kondisi tidak memenuhi, blok elseakan dijalankan.
print('')
x = 7
if x > 10:
    print("x lebih besar dari 10")
elif x > 5:
    print("x lebih besar dari 5 tapi kurang dari atau sama dengan 10")
else:
    print("x kurang dari atau sama dengan 5")


#if bersarang/ pencabangan bersarang
print('')
x = 15
if x > 10:
    print("x lebih besar dari 10")
    if x > 20:
        print("x juga lebih besar dari 20")
    else:
        print("x tidak lebih besar dari 20")

#operator terner
x = 8
result = "Lebih besar dari 5" if x > 5 else "Tidak lebih besar dari 5"
print(result)
