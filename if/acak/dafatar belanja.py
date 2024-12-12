def daftar_belanja():
    belanja = []
    while True:
        item = input("Masukkan item belanja (atau ketik 'selesai' untuk keluar): ")
        if item.lower() == 'selesai':
            break
        belanja.append(item)
    print("Daftar belanja Anda:", belanja)

daftar_belanja()