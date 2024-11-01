def nama_bulan(bulan):

  if bulan == 1:
    return "Januari"
  elif bulan == 2:
    return "Februari"
  elif bulan == 3:
    return "Maret"
  elif bulan == 4:
    return "april"
  elif bulan == 5:
    return "mei"
  elif bulan == 6:
    return "juni"
  elif bulan == 7:
    return "juli"
  elif bulan == 8:
    return "agustus"
  elif bulan == 9:
    return "september"
  elif bulan == 10:
    return "oktober"
  elif bulan == 11:
    return "november"
  elif bulan == 12:
    return "desember"
  else:
    return "Nomor bulan tidak valid"

bulan = int(input("Masukkan nomor bulan (1-12): "))

print(nama_bulan(bulan))