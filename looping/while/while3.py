jumlah = 0
while True:
    angka = int(input("Masukkan angka (0 untuk berhenti): "))
    if angka == 0:
        break
    if angka > 0:
        jumlah += angka
print("Jumlah bilangan positif:", jumlah)