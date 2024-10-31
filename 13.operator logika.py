#operator logika 

#digunakna untuk melakukann konjungsi (AND), Disjungsi(OR), negasi(NOT)
#operasi harus bertipe boolean
#menghasilkan type boolean= true or false

#operator AND (and) = hanya akan menghasilkan true jjika kedua operasi bernilai true
print('')
print('hasil true and true =', True and True)
print('hasil true and false =', True and False)
print('hasil false and true =', False and True)
print('hasil false and false =', False and False)

#operasi OR (or) = Hanya akan menghasilkan false jika kedua operasi bernilai false
print('')
print('hasil true and true =', True and True)
print('hasil true and false =', True and False)
print('hasil false and true =', False and True)
print('hasil false and false =', False and False)

#operasi NOT (not) = bernilai kebalikan
print('')
print('hasil not true =', not True)
print('hasil not false =', not False)

#pengaplikasian operasi and,or dan not
print('')
hasil = (6 > 6) and (9 <= 8)
print('(6 > 6) and (9 <= 8) =',hasil)
 
print('')
hasil = ('yadit' == 'yadit') or (12 <= 8)
print('(yadit == yadit) or (12 <= 8) =',hasil)
 
print('')
hasil = not (5 < 5)
print('not (5 < 5) =',hasil)

print('')
hasil = ('yadit' == 'yadit') and (12 <= 4) or (6 != 6)
print('(yadit' == 'yadit) and (12 <= 4) or (6 != 6) =',hasil)