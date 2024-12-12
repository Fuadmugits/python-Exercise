def pengelola_tugas():
    tugas = []
    while True:
        tugas_input = input("Masukkan tugas (atau ketik 'selesai' untuk keluar): ")
        if tugas_input.lower() == 'selesai':
            break
        tugas.append(tugas_input)
    print("Daftar tugas Anda:")
    for t in tugas:
        print(t)

pengelola_tugas()