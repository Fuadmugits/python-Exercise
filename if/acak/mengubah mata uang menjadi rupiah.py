def konversi_mata_uang():
    jumlah = float(input("Masukkan jumlah dalam USD: "))
    kurs = 15000  # Contoh kurs USD ke IDR
    idr = jumlah * kurs
    print(f"{jumlah} USD = {idr} IDR")

konversi_mata_uang()