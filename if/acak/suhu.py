def celsius_ke_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_ke_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Konversi Suhu")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")

pilihan = input("Pilih operasi (1/2): ")

if pilihan == '1':
    celsius = float(input("Masukkan suhu dalam Celsius: "))
    print(f"{celsius}°C = {celsius_ke_fahrenheit(celsius)}°F")
elif pilihan == '2':
    fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
    print(f"{fahrenheit}°F = {fahrenheit_ke_celsius(fahrenheit)}°C")
else:
    print("Pilihan tidak valid")