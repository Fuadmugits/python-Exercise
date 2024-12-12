n = int(input("Masukkan angka: "))
faktorial = 1
i = 1
while i <= n:
    faktorial *= i
    i += 1
print(f"Faktorial dari {n} adalah {faktorial}")