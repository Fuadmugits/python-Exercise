def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

angka = int(input("Masukkan angka untuk dihitung faktorialnya: "))
print(f"Faktorial dari {angka} adalah {faktorial(angka)}")