def urutkan_daftar():
    angka = input("Masukkan angka yang dipisahkan dengan koma: ")
    daftar = [int(x) for x in angka.split(',')]
    daftar.sort()
    print("Daftar yang diurutkan:", daftar)

urutkan_daftar()