def baca_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            isi = file.read()
            print(isi)
    except FileNotFoundError:
        print("File tidak ditemukan.")

baca_file('contoh.txt') 