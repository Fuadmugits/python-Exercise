def jumlah_hari_bulan(bulan, tahun):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        return 29 if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0) else 28
    else:
        return "Bulan tidak valid"

print(jumlah_hari_bulan(2, 2020))  