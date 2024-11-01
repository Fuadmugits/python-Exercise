print('='*45)
print('balok')
print('='*45)

p = int(input('masukan panjang balok :'))
t = int(input('masukan tinggi balok :'))
l = int(input('masukan lebar balok :'))

luas_balok = 2 * p * l + p * l + l * t
keliling_balok = 4 * p + l + t
volume_balok = p * l * t

print('hasil luas balok adalah :',luas_balok)
print('hasil keliling balok adalah :',keliling_balok)
print('hasil volume balok adalah :',volume_balok)