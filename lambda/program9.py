def balok():
    p = int(input('masukan nilai panjang: '))
    l = int(input('masukan nilai luas: '))
    t = int(input('masukan nilai tinggi: '))

    v = lambda : p * l * t
    print(v())
balok()