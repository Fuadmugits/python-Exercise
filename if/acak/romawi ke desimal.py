def romawi_ke_desimal(romawi):
    romawi_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    desimal = 0
    for i in range(len(romawi)):
        if i > 0 and romawi_dict[romawi[i]] > romawi_dict[romawi[i - 1]]:
            desimal += romawi_dict[romawi[i]] - 2 * romawi_dict[romawi[i - 1]]
        else:
            desimal += romawi_dict[romawi[i]]
    return desimal

romawi = input("Masukkan angka Romawi: ")
print(f"Angka desimal: {romawi_ke_desimal(romawi)}")