 #operator bitwise, operasi biner, binary
 
a = 9
b = 5

# bitwise OR 
c = a + b
print('/n==========OR==========')
print('nilai :',a,' binary :',format(a,'08b'))
print('nilai :',b,' binary :',format(b,'08b'))
print('_______________________________________')
print('nilai :',c,' binary :',format(c,'08b'))

#bitwise AND (&)
print('')
c = a & b
print('/n==========AND==========')
print('nilai :',a,' binary :',format(a,'08b'))
print('nilai :',b,' binary :',format(b,'08b'))
print('_______________________________________')
print('nilai :',c,' binary :',format(c,'08b'))


#bitwise XOR 
print('')
print('/n==========XOR==========')
print('nilai :',a,' binary :',format(a,'08b'))
print('nilai :',b,' binary :',format(b,'08b'))
print('_______________________________________')
print('nilai :',c,' binary :',format(c,'08b'))

#bitwise NOT
print('')
c  = ~a
print('/n==========NOT==========')
print('nilai :',a,' binary :',format(a,'08b'))
print('_______________________________________(~)')
print('nilai :',c,' binary :',format(c,'08b'))
print('_______________________________________(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :',e^d,' binary :',format(e^d,'08b'))