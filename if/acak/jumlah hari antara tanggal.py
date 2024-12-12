from datetime import datetime

def hitung_hari():
    tanggal1 = input("Masukkan tanggal pertama (YYYY-MM-DD): ")
    tanggal2 = input("Masukkan tanggal kedua (YYYY-MM-DD): ")
    t1 = datetime.strptime(tanggal1, "%Y-%m-%d")
    t2 = datetime.strptime(tanggal2, "%Y-%m-%d")
    selisih = abs((t2 - t1).days)
    print(f"Jumlah hari antara: {selisih} hari")