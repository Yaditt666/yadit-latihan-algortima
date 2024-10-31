# Membuat list dengan berbagai tipe data
my_list = [10, 20, 30, "yadit", True]

# Mengakses elemen dalam list
print("Elemen pertama:", my_list[0])  
print("Elemen terakhir:", my_list[-1])  

# Mengubah elemen pada indeks tertentu
my_list[1] = 50
print("List setelah mengubah elemen:", my_list) 
# Menambahkan elemen baru ke akhir list,menggunakan (append) untuk menambahkan elemen baru
my_list.append("Baru")
print("List setelah penambahan elemen:", my_list)  
# Menghapus elemen berdasarkan nilai,menggunakan (.remove) untuk menghapus elemen di list
my_list.remove(30)
print("List setelah penghapusan elemen:", my_list) 

# Mengakses elemen dengan indeks negatif
print("Elemen terakhir:", my_list[-1])  

# Mengurutkan list angka
angka_list = [3, 1, 4, 2, 5]
#menggunakan (sort)untuk mengurutkan list angka
angka_list.sort()
print("List setelah diurutkan:", angka_list) 
# Membalik urutan elemen dalam list
angka_list.reverse()
print("List setelah dibalik:", angka_list)  

# Menggabungkan dua list
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_gabungan = list_1 + list_2
print("List gabungan:", list_gabungan)  # Output: [1, 2, 3, 4, 5, 6]
