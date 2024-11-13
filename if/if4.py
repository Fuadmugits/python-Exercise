umur = int(input("masukan umur anda : "))

if umur < 12:
    print("kanak-kanak")
elif umur < 24:
    print("remaja")
elif umur < 60:
    print("dewasa")
elif umur < 120:
    print('tua')
else:
    print(" maaf umur valid ")
print(umur)