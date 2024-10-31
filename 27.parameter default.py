#parameter default pada function
def greet(nama="elvy"):
    print(f"Halo, {nama}!")

# Memanggil fungsi tanpa argumen menggunakan nilai default
greet()  

# Memanggil fungsi dengan argumen, yang akan menggantikan nilai default
greet("yadit")  
print('')
def order(menu="kopi", jumlah=1):
    print(f"Pesanan Anda: {jumlah} {menu}")

# Memanggil fungsi dengan nilai default
order() 

# Mengganti hanya satu parameter
order("teh")  

# Mengganti semua parameter
order("cokelat", 2)  
