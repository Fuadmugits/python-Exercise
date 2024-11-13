diskon_cukur = int(input("masukan umur anda"))

if diskon_cukur < 12:
    print("7000")
elif diskon_cukur <24:
    print("10000")
elif diskon_cukur >24:
    print("15000")
else:
    print("maaf anda tidak mendapatkan diskon")
print(diskon_cukur)