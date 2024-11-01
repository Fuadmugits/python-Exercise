def segitiga_sama_kaki():
    phi = 1/2

    alas = int(input('masukan alas: '))
    tinggi = int(input('masukan tinggi: '))

    l = lambda : phi * alas * tinggi
    print(l())
segitiga_sama_kaki()