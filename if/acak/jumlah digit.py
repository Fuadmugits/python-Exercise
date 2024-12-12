def jumlah_digit(angka):
    return sum(int(digit) for digit in str(angka))

angka = int(input("Masukkan angka: "))
print(f"Jumlah digit dari {angka} adalah {jumlah_digit(angka)}")