def hitung_rata_rata(daftar_angka):
    return sum(daftar_angka) / len(daftar_angka)

angka = []
n = int(input("Berapa banyak angka yang ingin Anda masukkan? "))

for i in range(n):
    angka.append(float(input(f"Masukkan angka ke-{i+1}: ")))

rata_rata = hitung_rata_rata(angka)
print(f"Rata-rata dari angka yang dimasukkan adalah: {rata_rata}")