import time

def pengingat():
    waktu = int(input("Masukkan waktu dalam detik untuk pengingat: "))
    print("Pengingat diatur...")
    time.sleep(waktu)
    print("Waktu pengingat telah tiba!")

pengingat()