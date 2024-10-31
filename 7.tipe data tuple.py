# Membuat tuple
tuple = (1, 2, 3, "yadit", True)

# Mengakses elemen dalam tuple
print(tuple[0])  
print(tuple[-1])  

# Tuple dalam tuple (nested tuple)
nested_tuple = (1, (2, 3), (4, 5))
print(nested_tuple[1]) 

# Menghitung jumlah elemen tertentu dalam tuple
print(tuple.count(1))  

# Mencari indeks elemen
print(tuple.index("yadit"))