import random

def batu_gunting_kertas():
    pilihan = ['batu', 'gunting', 'kertas']
    komputer = random.choice(pilihan)
    pemain = input("Pilih batu, gunting, atau kertas: ")

    if pemain == komputer:
        print(f"Boleh juga sama {pemain}. Seri!")
    elif (pemain == 'batu' and komputer == 'gunting') or \
         (pemain == 'gunting' and komputer == 'kertas') or \
         (pemain == 'kertas' and komputer == 'batu'):
        print(f"Selamat anda menang! Good Game Bro {komputer}.")
    else:
        print(f"Cih mengecewakan kalah oleh komputer {komputer}.")

batu_gunting_kertas()