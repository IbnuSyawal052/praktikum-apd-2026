


def judul(teks):
    print(f"\n{'=' * 50}")
    print(teks)
    print("=" * 50)
    for key, value in data.items():
        print(f"  {key:<10}: {value}")


def input_teks(pertanyaan):
    while True:
        jawaban = input(pertanyaan).strip()
        if jawaban:
            return jawaban
        print("  Input tidak boleh kosong, coba lagi.")


def input_semester(pertanyaan, boleh_kosong=False):
    while True:
        jawaban = input(pertanyaan).strip()
        if boleh_kosong and jawaban == "":
            return None
        try:
            nilai = int(jawaban)
            if nilai > 0:
                return nilai
            print("  Semester harus lebih dari 0.")
        except ValueError:
            print("  Semester harus berupa angka, coba lagi.")


def cari_key(data, nama):
    for key in data:
        if key.lower() == nama.lower():
            return key
    return None


def tambah_key(data):
    judul("TAMBAH DATA")
    nama_key = input_teks("  Nama key yang ditambahkan (mis. alamat): ")
    if cari_key(data, nama_key):
        print(f"  Key '{nama_key}' sudah ada. Pilih key lain.")
        return
    data[nama_key] = input_teks(f"  Isi nilai untuk '{nama_key}': ")
    print(f"  Berhasil menambahkan '{nama_key}'.")


def ubah_semester(data):
    judul("UBAH SEMESTER")
    print(f"  Semester saat ini: {data['semester']}")
    baru = input_semester(
        "  Semester baru (tekan Enter = semester berikutnya): ",
        boleh_kosong=True,
    )
    lama = data["semester"]
    data["semester"] = lama + 1 if baru is None else baru
    print(f"  Semester {lama} -> semester {data['semester']}")


def hapus_key(data):
    judul("HAPUS DATA")
    print("  Key yang tersedia:", ", ".join(data.keys()))
    nama_key = input_teks("  Key yang ingin dihapus: ")
    key_asli = cari_key(data, nama_key)
    if key_asli is None:
        print(f"  Key '{nama_key}' tidak ditemukan.")
        return
    if key_asli == "semester":
        print("  Key 'semester' dibutuhkan menu ubah semester, jadi tidak bisa dihapus.")
        return
    nilai = data.pop(key_asli)
    print(f"  Key '{key_asli}' dihapus (nilainya: {nilai}).")


def tampilkan_menu():
    print("\n--- MENU ---")
    print("1. Tambah data (key baru)")
    print("2. Ubah semester")
    print("3. Hapus data (key)")
    print("4. Tampilkan jumlah item")
    print("5. Tampilkan semua isi")
    print("0. Keluar")


# Membuat dictionary awal dari input pengguna
print("=== DATA MAHASISWA ===")
mahasiswa = {
    "nama": input_teks("Masukkan nama     : "),
    "NIM": input_teks("Masukkan NIM      : "),
    "prodi": input_teks("Masukkan prodi    : "),
    "semester": input_semester("Masukkan semester : "),
}

# Perulangan menu: berjalan terus sampai pengguna memilih 0
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (0-5): ").strip()

    if pilihan == "1":
        tambah_key(mahasiswa)
    elif pilihan == "2":
        ubah_semester(mahasiswa)
    elif pilihan == "3":
        hapus_key(mahasiswa)
    elif pilihan == "4":
        judul("JUMLAH ITEM")
        print(f"  Jumlah item: {len(mahasiswa)}")
    elif pilihan == "5":
        judul("ISI DICTIONARY")
        for key, value in mahasiswa.items():
            print(f"  {key}: {value}")
    elif pilihan == "0":
        judul("DATA AKHIR")
        for key, value in mahasiswa.items():
            print(f"  {key}: {value}")
        print("\nTerima kasih, program selesai.")
        break
    else:
        print("  Pilihan tidak valid, masukkan angka 0-5.")