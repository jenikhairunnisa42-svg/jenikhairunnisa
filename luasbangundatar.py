import math

print("=== PROGRAM LUAS BANGUN DATAR ===")
print("1. Lingkaran")
print("2. Persegi Panjang")
print("3. Segitiga")

pilihan = int(input("Pilih bangun datar (1/2/3): "))

if pilihan == 1:
    r = float(input("Masukkan jari-jari: "))
    luas = math.pi * r ** 2
    print("Luas lingkaran =", luas)

elif pilihan == 2:
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    print("Luas persegi panjang =", luas)

elif pilihan == 3:
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = 0.5 * alas * tinggi
    print("Luas segitiga =", luas)

else:
    print("Pilihan tidak tersedia.")
