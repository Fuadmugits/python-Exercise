import random

angka_rahasia = random.randint(1, 100)
tebakan = None

print("Selamat datang di permainan tebak angka!")
print("Saya telah memilih angka antara 1 dan 100. Coba tebak!")

while tebakan != angka_rahasia:
    tebakan = int(input("Masukkan tebakan Anda: "))
    if tebakan < angka_rahasia:
        print("Tebakan Anda terlalu rendah. Coba lagi!")
    elif tebakan > angka_rahasia:
        print("Tebakan Anda terlalu tinggi. Coba lagi!")
    else:
        print("Selamat! Anda telah menebak angka yang benar!")