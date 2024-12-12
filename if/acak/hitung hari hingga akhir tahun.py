from datetime import datetime

def hitung_hari_tahun_baru():
    hari_ini = datetime.now()
    tahun_baru = datetime(hari_ini.year + 1, 1, 1)
    selisih = tahun_baru - hari_ini
    print(f"Hari hingga Tahun Baru: {selisih.days} hari")

hitung_hari_tahun_baru()