import json
import os

# Nama file untuk menyimpan data pasien
FILE_DATA = "data_pasien.json"


# Membaca data pasien yang sudah tersimpan
def baca_data():
    if os.path.exists(FILE_DATA):
        with open(FILE_DATA, "r") as file:
            return json.load(file)
    return []


# Menyimpan data pasien ke file JSON
def simpan_data(data):
    with open(FILE_DATA, "w") as file:
        json.dump(data, file, indent=4)


# Registrasi pasien baru
def registrasi():
    print("\n=== REGISTRASI PASIEN KLINIK ===")

    data = baca_data()

    # Memasukkan identitas pasien
    pasien = {
        "id_pasien": input("ID Pasien: "),
        "nama": input("Nama lengkap: "),
        "tanggal_lahir": input("Tanggal lahir: "),
        "jenis_kelamin": input("Jenis kelamin: "),
        "alamat": input("Alamat: "),
        "no_hp": input("Nomor HP: "),
        "keluhan": input("Keluhan pasien: "),
        "tanggal_kunjungan": input("Tanggal kunjungan: "),
        "dokter": input("Nama dokter: ")
    }

    # Menambahkan pasien ke daftar
    data.append(pasien)
    simpan_data(data)

    print("\nRegistrasi pasien berhasil!")


# Menampilkan semua pasien
def tampilkan_data():
    data = baca_data()

    print("\n=== DAFTAR PASIEN KLINIK ===")

    if not data:
        print("Belum ada data pasien.")
        return

    for nomor, pasien in enumerate(data, start=1):
        print(f"\n--- Pasien {nomor} ---")

        for kolom, isi in pasien.items():
            print(f"{kolom.replace('_', ' ').title()}: {isi}")


# Mencari pasien berdasarkan ID
def cari_pasien():
    data = baca_data()
    id_cari = input("Masukkan ID pasien: ")

    for pasien in data:
        if pasien["id_pasien"] == id_cari:
            print("\n=== DATA PASIEN DITEMUKAN ===")

            for kolom, isi in pasien.items():
                print(f"{kolom.replace('_', ' ').title()}: {isi}")
            return

    print("Data pasien tidak ditemukan.")


# Menghapus data berdasarkan ID pasien
def hapus_pasien():
    data = baca_data()
    id_hapus = input("Masukkan ID pasien yang dihapus: ")

    data_baru = [
        pasien for pasien in data
        if pasien["id_pasien"] != id_hapus
    ]

    if len(data_baru) < len(data):
        simpan_data(data_baru)
        print("Data pasien berhasil dihapus.")
    else:
        print("ID pasien tidak ditemukan.")


# Menu utama program
while True:
    print("\n===== SISTEM REGISTRASI KLINIK =====")
    print("1. Registrasi pasien")
    print("2. Lihat semua pasien")
    print("3. Cari pasien")
    print("4. Hapus pasien")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        registrasi()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        cari_pasien()
    elif pilihan == "4":
        hapus_pasien()
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")