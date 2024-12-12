print("="*50)
print('\tMENGHITUNG TUKARAN PECAHAN UANG')
print("="*50)

nilai_uang = int(input('Masukkan nilai uang (dalam kelipatan 25): '))

jumlah_1000 = nilai_uang // 1000
nilai_uang %= 1000
jumlah_500 = nilai_uang // 500
nilai_uang %= 500
jumlah_100 = nilai_uang // 100
nilai_uang %= 100
jumlah_50 = nilai_uang // 50
nilai_uang %= 50
jumlah_25 = nilai_uang // 25

print('Pecahan uang yang tersedia:')
print(jumlah_1000, 'pecahan Rp1000')
print(jumlah_500, 'pecahan Rp500')
print(jumlah_100, 'pecahan Rp100')
print(jumlah_50, 'pecahan Rp50')
print(jumlah_25, 'pecahan Rp25')
