def prisma():
    phi = 1/2

    p = int(input('masukan nilai panjang: '))
    l = int(input('masukan nilali luas: '))
    t = int(input('masukan nilai tinggi'))

    v = lambda : phi * p * l * t
    print(v())
prisma()