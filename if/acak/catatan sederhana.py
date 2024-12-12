def catatan():
    catatan_list = []
    while True:
        catatan_input = input("Masukkan catatan (atau ketik 'selesai' untuk keluar): ")
        if catatan_input.lower() == 'selesai':
            break
        catatan_list.append(catatan_input)
    print("Catatan Anda:")
    for cat in catatan_list:
        print(cat)

catatan()