print("="*45)
print("nilai murid")
print("="*45)

def tentukan_indeks(nilai):
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"
    
nilai_ujian = float(input("masukan jumlah nilai\t :"))
indeks_nilai = tentukan_indeks(nilai_ujian)

print("indeks nilai anda adalah:",indeks_nilai)