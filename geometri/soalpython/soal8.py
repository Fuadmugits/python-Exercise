print('*'*48)
print('\t\tPROGAM TABUNG')
print("*"*48)

r = int(input('masukan nilai jari jari\t;'))
tinggi = int(input('masukan nilai tinggi\t:'))

volume = 3.14 * r * r * tinggi 
lp = 2 * 3.14
AA = r + tinggi

print('volume\t\t:', volume,'cm2')
print('luas permukaan\t\t:' , lp * AA, 'cm2')