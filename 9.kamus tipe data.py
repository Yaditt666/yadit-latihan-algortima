#tipe data Dictionary/kamus python,yang berfungsi untuk menyimpan kumpulan data
print("python dictionary")
#1,menggunakan kurung kurawal
print('')#baris baru
yadit = {"NAMA" : "YADIT", "PRODI" : "SISTEM INFORMASI", "NIM" : "D0424306", "IPK" : "3.90"}
#cara mengakses pemanggilan
print("1.cara akses item pemanggilan")
print(yadit)
print( "-Nama:", yadit["NAMA"])
print( "-Prodi:", yadit["PRODI"])
print( "-NIM:", yadit["NIM"])
print( "-IPK:", yadit["IPK"])

print('')
#menggunakan dictionary/rungsi dictioanry
yadit = dict(
    nama = "Yadit", nim = "D0424306", prodi = "Sistem Informasi"
)
print("2.Cara Akses Item Pemanggilan")
print("Nama=", yadit.get("nama"))
print("Nim=", yadit.get("nim"))
print("Prodi=", yadit.get("prodi"))

print('')
#metode kamus python menggunakan update
print("3.menggunakan update")
yadit.update ({"ipk" : "3.90"})
print(yadit)