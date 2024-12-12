def bilangan_genap(n):
    return [i for i in range(1, n + 1) if i % 2 == 0]

n = int(input("Masukkan angka N: "))
genap = bilangan_genap(n)
print(f"Bilangan genap dari 1 hingga {n}: {genap}")