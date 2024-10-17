def segitiga():
    phi = 0,5

    alas = int(input('masukan nilai alas: '))
    tinggi = int(input('masukan nilai tinggi: '))

    l = lambda : phi * alas * tinggi
    print(l())
segitiga()