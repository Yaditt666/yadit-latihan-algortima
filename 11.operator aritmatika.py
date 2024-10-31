#operasi aritmatika

a = 10
b = 3


#operator perjumlahan +
print('')
hasil = a + b
print(a,'+',b,'=',hasil)

#operator pengurangan -
print('')
hasil = a - b
print(a,'-',b,'=',hasil)

#operator perkalian *
print('')
hasil = a * b
print(a,'*',b,'=',hasil)

#operator pembagian /
print('')
hasil = a / b
print(a,'/',b,'=',hasil)

#operator pembagian bulat (floor) //
print('')
hasil = a // b
print(a,'//',b,'=',hasil)

#operator sisa bagi (modulus) %
print('')
hasil = a % b
print(a,'%',b,'=',hasil)

#operator pemangkatan (eksponen ) **
print('')
hasil = a ** b
print(a,'**',b,'=',hasil)

#prioritas aritmatika
x = 3
y = 2
z = 4

hasil = x  ** y * z + x / y - y % z // x
print(x,'**' ,y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, '=' ,hasil) 