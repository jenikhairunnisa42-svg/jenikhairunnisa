# Program Menghitung Suhu Udara
print("=== PROGRAM SUHU UDARA ===")

# Memasukkan Suhu dalam Celcius
celcius = float (input("Masukkan suhu dalam Celcius: "))
# Menghitung Fahrenheit
fahrenheit = (celcius *9/5) + 32
# Menghitung Reamur
reamur = celcius* 4/5

# Menentukan kondisi suhu
if celcius < 20 :
    kondisi = "Dingin"
elif celcius <= 30 :
    kondisi = "Normal"
else:
    kondisi = "Panas"

#Menampilkan hasil
print("\n=== HASIL PERHITUNGAN ===")
print("Suhu Celcius :", celcius, "C")
print("Suhu Fahrenheit :", fahrenheit, "F")
print("Suhu Reamur :", reamur, "R")
print("Kondisi Suhu :", kondisi)