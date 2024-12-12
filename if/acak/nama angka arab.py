print('='*50)
print('\t\tANGKA ARAB')
print('='*50)

angka_arab = [
    "١ (waahidun)",
    "٢ (itsnaani)",
    "٣ (thalaatsatun)",
    "٤ (arba'atun)",
    "٥ (khomsatun)",
    "٦ (sittatun)",
    "٧ (sab'atun)",
    "٨ (tsamaniyatun)",
    "٩ (tis'atun)",
    "١٠ ('asyratun)",
    "١١ (ahad ashara)",
    "١٢ (itsna ashara)",
    "١٣ (thalaatsata 'asyara)",
    "١٤ (arba'ata 'asyara)",
    "١٥ (khomsata 'asyara)"
]

angka = int(input('Masukkan angka 1-15 \t\t: '))

if 1 <= angka <= 15:
    print(f'{angka} dalam angka Arab adalah\t: {angka_arab[angka-1]}')
else:
    print('Angka salah. Tolong masukkan angka 1-15.')
