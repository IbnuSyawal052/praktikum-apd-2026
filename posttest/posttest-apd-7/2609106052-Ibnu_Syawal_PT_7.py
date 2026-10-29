# Perintah clear terminal (otomatis menyesuaikan dengan OS pengguna)
import os


perintah_clear = "cls" if os.name == "nt" else "clear"

# Database (Variabel Global)

# dictionary user {username: {"password": , "role": }}
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
}

# dictionary produk : {id: {"nama": , "kategori": , "harga": , "stok": }}
produk = {
    1: {"nama": "Intel Core i5-12400F", "kategori": "Processor", "harga": 2100000, "stok": 15},
    2: {"nama": "AMD Ryzen 5 5600", "kategori": "Processor", "harga": 1900000, "stok": 12},
    3: {"nama": "ASUS Prime B660M-K", "kategori": "Motherboard", "harga": 1750000, "stok": 8},
    4: {"nama": "Corsair Vengeance 16GB DDR4", "kategori": "RAM", "harga": 750000, "stok": 20},
    5: {"nama": "Samsung 980 NVMe 500GB", "kategori": "SSD", "harga": 850000, "stok": 18},
    6: {"nama": "NVIDIA RTX 4060 8GB", "kategori": "VGA", "harga": 5500000, "stok": 6},
    7: {"nama": "Corsair CV650 650W", "kategori": "PSU", "harga": 900000, "stok": 10},
}
# untuk menghitung id produk otomatis
id_berikutnya = 8

# kode riwayat pembelian {id: {"username": , "produk": , "jumlah": , "total": }}
riwayat = {}
# untuk menghitung id riwayat otomatis
id_riwayat = 1

# daftar kategori yang boleh dipakai
daftar_kategori = ["Processor", "GPU", "RAM", "SSD", "Motherboard", "VGA", "PSU"]

# username yang sedang login (None = belum ada yang login)
user_aktif = None


# FUNGSI TANPA PARAMETER

def menu_utama():
    os.system(perintah_clear)
    print("=" * 60)
    print("        TOKO KOMPONEN PC - SISTEM MANAJEMEN")
    print("=" * 60)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("-" * 60)
    return input("Pilih menu: ").strip()


def menu_admin():
    os.system(perintah_clear)
    print("=" * 60)
    print(f"  MENU ADMIN  |  Login sebagai: {user_aktif}")
    print("=" * 60)
    print("1. Lihat Semua Produk")
    print("2. Tambah Produk")
    print("3. Ubah Produk")
    print("4. Hapus Produk")
    print("5. Cari Produk")
    print("6. Lihat Daftar Pengguna")
    print("7. Hapus Pengguna")
    print("8. Riwayat Semua Transaksi")
    print("0. Logout")
    print("-" * 60)
    return input("Pilih menu: ").strip()


def menu_pengguna():
    os.system(perintah_clear)
    print("=" * 60)
    print(f"  MENU PENGGUNA  |  Login sebagai: {user_aktif}")
    print("=" * 60)
    print("1. Lihat Semua Produk")
    print("2. Cari Produk")
    print("3. Beli Produk")
    print("4. Riwayat Pembelian Saya")
    print("5. Ubah Password")
    print("0. Logout")
    print("-" * 60)
    return input("Pilih menu: ").strip()


def total_pendapatan():
    # menjumlahkan total semua transaksi pakai fungsi rekursif
    return hitung_total(list(riwayat.values()), 0)


# FUNGSI DENGAN PARAMETER

def format_rupiah(angka):
    return "Rp" + f"{angka:,}".replace(",", ".")


def ubah_ke_angka(teks, nama_field, minimal):
    # mengubah input ke integer, kalau gagal akan memunculkan error
    try:
        angka = int(teks)
    except ValueError:
        raise ValueError(f"{nama_field} harus berupa angka bulat!")
    if angka < minimal:
        raise ValueError(f"{nama_field} minimal {minimal}!")
    return angka


def cari_produk(kata_kunci):
    hasil = {}
    for id_p, p in produk.items():
        if kata_kunci in p["nama"].lower() or kata_kunci in p["kategori"].lower():
            hasil[id_p] = p
    return hasil


# FUNGSI REKURSIF
def hitung_total(daftar, i):
    # daftar = list transaksi, i = index yang sedang dihitung
    if i == len(daftar):
        return 0
    return daftar[i]["total"] + hitung_total(daftar, i + 1)


# PROSEDUR

def tampil_tabel(data):
    if len(data) == 0:
        print("Belum ada produk.")
    else:
        print(f"{'ID':<5}{'Nama':<32}{'Kategori':<14}{'Harga':>14}{'Stok':>7}")
        print("-" * 72)
        for id_p, p in data.items():
            print(f"{id_p:<5}{p['nama']:<32}{p['kategori']:<14}{format_rupiah(p['harga']):>14}{p['stok']:>7}")


def lihat_produk():
    os.system(perintah_clear)
    print("=== DAFTAR PRODUK ===")
    tampil_tabel(produk)
    input("\nTekan Enter untuk kembali...")


def tambah_produk():
    global id_berikutnya
    os.system(perintah_clear)
    print("=== TAMBAH PRODUK ===")
    try:
        nama = input("Nama produk  : ").strip()
        kategori = input("Kategori (Processor, GPU, RAM, SSD, Motherboard, VGA, PSU)    : ").strip()
        harga_str = input("Harga (Rp)                      : ").strip()
        stok_str = input("Stok                            : ").strip()

        if nama == "" or kategori == "":
            raise ValueError("Nama dan kategori tidak boleh kosong!")
        if len(nama) > 30:
            raise ValueError("Nama produk maksimal 30 karakter!")
        if kategori not in daftar_kategori:
            raise ValueError("Kategori tidak terdaftar!")
        for p in produk.values():
            if p["nama"].lower() == nama.lower():
                raise ValueError("Produk dengan nama tersebut sudah ada!")
        harga = ubah_ke_angka(harga_str, "Harga", 1)
        stok = ubah_ke_angka(stok_str, "Stok", 0)
    except ValueError as e:
        print(f"\n[!] {e}")
    else:
        produk[id_berikutnya] = {
            "nama": nama,
            "kategori": kategori,
            "harga": harga,
            "stok": stok,
        }
        print(f"\n[+] Produk '{nama}' berhasil ditambahkan dengan ID {id_berikutnya}.")
        id_berikutnya += 1
    finally:
        input("Tekan Enter untuk kembali...")


def ubah_produk():
    os.system(perintah_clear)
    print("=== UBAH PRODUK ===")
    try:
        if len(produk) == 0:
            raise ValueError("Belum ada produk.")
        tampil_tabel(produk)

        id_str = input("\nMasukkan ID produk yang ingin diubah: ").strip()
        id_produk = ubah_ke_angka(id_str, "ID", 1)
        target = produk[id_produk]

        print("\n(Kosongkan lalu tekan Enter jika tidak ingin mengubah)")
        nama_baru = input(f"Nama     [{target['nama']}]: ").strip()
        kategori_baru = input(f"Kategori [{target['kategori']}]: ").strip()
        harga_baru = input(f"Harga    [{target['harga']}]: ").strip()
        stok_baru = input(f"Stok     [{target['stok']}]: ").strip()

        if nama_baru != "" and len(nama_baru) > 30:
            raise ValueError("Nama produk maksimal 30 karakter!")
        if kategori_baru != "" and kategori_baru not in daftar_kategori:
            raise ValueError("Kategori tidak terdaftar!")
        if harga_baru != "":
            harga_baru = ubah_ke_angka(harga_baru, "Harga", 1)
        if stok_baru != "":
            stok_baru = ubah_ke_angka(stok_baru, "Stok", 0)
    except ValueError as e:
        print(f"\n[!] {e}")
        print("[!] Perubahan dibatalkan.")
    except KeyError:
        print("\n[!] Produk dengan ID tersebut tidak ditemukan!")
    else:
        if nama_baru != "":
            target["nama"] = nama_baru
        if kategori_baru != "":
            target["kategori"] = kategori_baru
        if harga_baru != "":
            target["harga"] = harga_baru
        if stok_baru != "":
            target["stok"] = stok_baru
        print("\n[+] Produk berhasil diperbarui.")
    finally:
        input("Tekan Enter untuk kembali...")


def hapus_produk():
    os.system(perintah_clear)
    print("=== HAPUS PRODUK ===")
    try:
        if len(produk) == 0:
            raise ValueError("Belum ada produk.")
        tampil_tabel(produk)

        id_str = input("\nMasukkan ID produk yang ingin dihapus: ").strip()
        id_produk = ubah_ke_angka(id_str, "ID", 1)
        target = produk[id_produk]
        konfirmasi = input(f"Yakin hapus '{target['nama']}'? (y/n): ").strip().lower()
    except ValueError as e:
        print(f"\n[!] {e}")
    except KeyError:
        print("\n[!] Produk dengan ID tersebut tidak ditemukan!")
    else:
        if konfirmasi == "y":
            del produk[id_produk]
            print("\n[+] Produk berhasil dihapus.")
        else:
            print("\n[i] Penghapusan dibatalkan.")
    finally:
        input("Tekan Enter untuk kembali...")


def menu_cari_produk():
    os.system(perintah_clear)
    print("=== CARI PRODUK ===")
    try:
        kata_kunci = input("Masukkan nama / kategori produk: ").strip().lower()
        if kata_kunci == "":
            raise ValueError("Kata kunci tidak boleh kosong!")
        hasil = cari_produk(kata_kunci)
    except ValueError as e:
        print(f"\n[!] {e}")
    else:
        if len(hasil) == 0:
            print("\nProduk tidak ditemukan.")
        else:
            print()
            tampil_tabel(hasil)
            print(f"\n{len(hasil)} produk ditemukan.")
    finally:
        input("\nTekan Enter untuk kembali...")


def lihat_pengguna():
    os.system(perintah_clear)
    print("=== DAFTAR PENGGUNA ===")
    print(f"{'No':<5}{'Username':<20}{'Password':<15}{'Role':<10}")
    print("-" * 50)
    nomor = 1
    for nama_user, data_user in users.items():
        print(f"{nomor:<5}{nama_user:<20}{'*' * len(data_user['password']):<15}{data_user['role']:<10}")
        nomor += 1
    input("\nTekan Enter untuk kembali...")


def hapus_pengguna():
    os.system(perintah_clear)
    print("=== HAPUS PENGGUNA ===")
    print(f"{'No':<5}{'Username':<20}{'Role':<10}")
    print("-" * 35)
    nomor = 1
    for nama_user, data_user in users.items():
        print(f"{nomor:<5}{nama_user:<20}{data_user['role']:<10}")
        nomor += 1

    try:
        nama_hapus = input("\nMasukkan username yang ingin dihapus: ").strip()
        if nama_hapus == "":
            raise ValueError("Username tidak boleh kosong!")
        if nama_hapus == user_aktif:
            raise ValueError("Anda tidak dapat menghapus akun yang sedang digunakan!")
        data_hapus = users[nama_hapus]
        konfirmasi = input(f"Yakin hapus pengguna '{nama_hapus}'? (y/n): ").strip().lower()
    except ValueError as e:
        print(f"\n[!] {e}")
    except KeyError:
        print("\n[!] Username tidak ditemukan!")
    else:
        if konfirmasi == "y":
            del users[nama_hapus]
            print("\n[+] Pengguna berhasil dihapus.")
        else:
            print("\n[i] Penghapusan dibatalkan.")
    finally:
        input("Tekan Enter untuk kembali...")


def riwayat_semua():
    os.system(perintah_clear)
    print("=== RIWAYAT SEMUA TRANSAKSI ===")
    try:
        if len(riwayat) == 0:
            raise ValueError("Belum ada transaksi.")
        print(f"{'No':<5}{'Pembeli':<15}{'Produk':<32}{'Jml':>5}{'Total':>16}")
        print("-" * 73)
        nomor = 1
        for r in riwayat.values():
            print(f"{nomor:<5}{r['username']:<15}{r['produk']:<32}{r['jumlah']:>5}{format_rupiah(r['total']):>16}")
            nomor += 1
        print("-" * 73)
        print(f"Total pendapatan: {format_rupiah(total_pendapatan())}")
    except ValueError as e:
        print(e)
    finally:
        input("\nTekan Enter untuk kembali...")


def beli_produk():
    global id_riwayat
    os.system(perintah_clear)
    print("=== BELI PRODUK ===")
    try:
        if len(produk) == 0:
            raise ValueError("Belum ada produk.")
        tampil_tabel(produk)

        id_str = input("\nMasukkan ID produk yang ingin dibeli: ").strip()
        id_produk = ubah_ke_angka(id_str, "ID", 1)
        target = produk[id_produk]
        if target["stok"] == 0:
            raise ValueError("Maaf, stok produk ini sedang habis!")

        print(f"\nProduk : {target['nama']}")
        print(f"Harga  : {format_rupiah(target['harga'])}")
        print(f"Stok   : {target['stok']}")
        jumlah = ubah_ke_angka(input("Jumlah beli: ").strip(), "Jumlah", 1)
        if jumlah > target["stok"]:
            raise ValueError(f"Stok tidak cukup! Stok tersedia: {target['stok']}")

        total = jumlah * target["harga"]
        konfirmasi = input(f"Total bayar {format_rupiah(total)}. Lanjutkan? (y/n): ").strip().lower()
    except ValueError as e:
        print(f"\n[!] {e}")
    except KeyError:
        print("\n[!] Produk dengan ID tersebut tidak ditemukan!")
    else:
        if konfirmasi == "y":
            target["stok"] -= jumlah
            riwayat[id_riwayat] = {
                "username": user_aktif,
                "produk": target["nama"],
                "jumlah": jumlah,
                "total": total,
            }
            id_riwayat += 1
            print("\n[+] Pembelian berhasil! Terima kasih.")
        else:
            print("\n[i] Pembelian dibatalkan.")
    finally:
        input("Tekan Enter untuk kembali...")


def riwayat_saya():
    os.system(perintah_clear)
    print("=== RIWAYAT PEMBELIAN SAYA ===")
    milik_sendiri = []
    for r in riwayat.values():
        if r["username"] == user_aktif:
            milik_sendiri.append(r)

    try:
        if len(milik_sendiri) == 0:
            raise ValueError("Anda belum pernah melakukan pembelian.")
        print(f"{'No':<5}{'Produk':<32}{'Jml':>5}{'Total':>16}")
        print("-" * 58)
        nomor = 1
        for r in milik_sendiri:
            print(f"{nomor:<5}{r['produk']:<32}{r['jumlah']:>5}{format_rupiah(r['total']):>16}")
            nomor += 1
        print("-" * 58)
        print(f"Total belanja: {format_rupiah(hitung_total(milik_sendiri, 0))}")
    except ValueError as e:
        print(e)
    finally:
        input("\nTekan Enter untuk kembali...")


def ubah_password():
    os.system(perintah_clear)
    print("=== UBAH PASSWORD ===")
    pass_lama = input("Password lama          : ").strip()
    pass_baru = input("Password baru          : ").strip()
    pass_konfirmasi = input("Konfirmasi password   : ").strip()
    try:
        if pass_lama != users[user_aktif]["password"]:
            raise ValueError("Password lama salah!")
        if len(pass_baru) < 6:
            raise ValueError("Password baru minimal 6 karakter!")
        if " " in pass_baru:
            raise ValueError("Password tidak boleh mengandung spasi!")
        if pass_baru != pass_konfirmasi:
            raise ValueError("Konfirmasi password tidak cocok!")
    except ValueError as e:
        print(f"\n[!] {e}")
    else:
        users[user_aktif]["password"] = pass_baru
        print("\n[+] Password berhasil diubah.")
    finally:
        input("Tekan Enter untuk kembali...")


def login():
    global user_aktif
    os.system(perintah_clear)
    print("=== LOGIN ===")
    username_input = input("Username : ").strip()
    password_input = input("Password : ").strip()
    try:
        if username_input not in users or users[username_input]["password"] != password_input:
            raise ValueError("Username atau password salah!")
    except ValueError as e:
        print(f"\n[!] {e}")
        input("Tekan Enter untuk kembali...")
    else:
        user_aktif = username_input


# REGISTER (akun baru otomatis akan diberi role pengguna biasa)
def register():
    os.system(perintah_clear)
    print("=== REGISTER AKUN BARU ===")
    username_baru = input("Username (min 4 karakter, tanpa spasi) : ").strip()
    password_baru = input("Password (min 6 karakter, tanpa spasi) : ").strip()
    password_ulang = input("Konfirmasi password                    : ").strip()
    try:
        if len(username_baru) < 4:
            raise ValueError("Username minimal 4 karakter!")
        if " " in username_baru:
            raise ValueError("Username tidak boleh mengandung spasi!")
        for nama_user in users:
            if nama_user.lower() == username_baru.lower():
                raise ValueError("Username sudah digunakan, silakan pilih yang lain!")
        if len(password_baru) < 6:
            raise ValueError("Password minimal 6 karakter!")
        if " " in password_baru:
            raise ValueError("Password tidak boleh mengandung spasi!")
        if password_baru != password_ulang:
            raise ValueError("Konfirmasi password tidak cocok!")
    except ValueError as e:
        print(f"\n[!] {e}")
    else:
        users[username_baru] = {"password": password_baru, "role": "user"}
        print(f"\n[+] Registrasi berhasil! Silakan login sebagai '{username_baru}'.")
    finally:
        input("Tekan Enter untuk kembali...")


# SESI LOGIN (MULTIUSER)

def sesi_admin():
    sesi_login = True
    while sesi_login:
        menu = menu_admin()

        if menu == "1":
            lihat_produk()
        elif menu == "2":
            tambah_produk()
        elif menu == "3":
            ubah_produk()
        elif menu == "4":
            hapus_produk()
        elif menu == "5":
            menu_cari_produk()
        elif menu == "6":
            lihat_pengguna()
        elif menu == "7":
            hapus_pengguna()
        elif menu == "8":
            riwayat_semua()
        elif menu == "0":
            sesi_login = False
        else:
            print("\n[!] Menu tidak valid! Pilih angka 0 - 8.")
            input("Tekan Enter untuk melanjutkan...")


def sesi_pengguna():
    sesi_login = True
    while sesi_login:
        menu = menu_pengguna()

        if menu == "1":
            lihat_produk()
        elif menu == "2":
            menu_cari_produk()
        elif menu == "3":
            beli_produk()
        elif menu == "4":
            riwayat_saya()
        elif menu == "5":
            ubah_password()
        elif menu == "0":
            sesi_login = False
        else:
            print("\n[!] Menu tidak valid! Pilih angka 0 - 5.")
            input("Tekan Enter untuk melanjutkan...")


# PROGRAM UTAMA

program_berjalan = True
while program_berjalan:
    pilihan = menu_utama()

    if pilihan == "1":
        login()
        if user_aktif is not None:
            if users[user_aktif]["role"] == "admin":
                sesi_admin()
            else:
                sesi_pengguna()
            user_aktif = None

    elif pilihan == "2":
        register()

    elif pilihan == "3":
        os.system(perintah_clear)
        print("Terima kasih telah menggunakan sistem ini. Sampai jumpa!")
        program_berjalan = False

    else:
        print("\n[!] Menu tidak valid! Pilih angka 1 - 3.")
        input("Tekan Enter untuk melanjutkan...")
