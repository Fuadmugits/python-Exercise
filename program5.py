def belah_ketupat():
    phi = 0.5
  
    d1 = float(input('masukan diagonal1: '))
    d2 = float(input('masukan diagonal2: '))

    l = lambda : phi * d1 * d2
    print(l())
belah_ketupat()