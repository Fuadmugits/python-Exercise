def max_min_daftar():
    angka = input("Masukkan angka yang dipisahkan dengan koma: ")
    daftar = [int(x) for x in angka.split(',')]
    print(f"Nilai maksimum: {max(daftar)}")
    print(f"Nilai minimum: {min(daftar)}")

max_min_daftar()