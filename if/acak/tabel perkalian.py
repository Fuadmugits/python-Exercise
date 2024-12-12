def tabel_perkalian(n):
    print(f"Tabel Perkalian {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

angka = int(input("Masukkan angka untuk tabel perkalian: "))
tabel_perkalian(angka)