from prettytable import PrettyTable

from database import state, users, riwayat
from halhalberguna import bersihkan_layar, format_rupiah, hitung_total


def _buat_tabel(kolom, rata_kanan=()):
    tabel = PrettyTable()
    tabel.field_names = kolom
    for k in kolom:
        tabel.align[k] = "r" if k in rata_kanan else "l"
    return tabel




def tampil_tabel_produk(data):
    if len(data) == 0:
        print("Belum ada produk.")
        return
    tabel = _buat_tabel(["ID", "Nama", "Kategori", "Harga", "Stok"], ("Harga", "Stok"))
    for id_p, p in data.items():
        tabel.add_row([id_p, p["nama"], p["kategori"], format_rupiah(p["harga"]), p["stok"]])
    print(tabel)


def tampil_tabel_pengguna(sembunyikan_password=True):
    kolom = ["No", "Username", "Role"]
    if sembunyikan_password:
        kolom.insert(2, "Password")
    tabel = _buat_tabel(kolom)
    for nomor, (nama, data) in enumerate(users.items(), start=1):
        baris = [nomor, nama, data["role"]]
        if sembunyikan_password:
            baris.insert(2, "********")
        tabel.add_row(baris)
    print(tabel)


def tampil_tabel_riwayat(daftar, semua=True):
    # semua=True -> tampilkan kolom Pembeli (untuk admin)
    kolom = ["No", "Waktu"]
    if semua:
        kolom.append("Pembeli")
    kolom += ["Produk", "Jml", "Total"]
    tabel = _buat_tabel(kolom, ("Jml", "Total"))
    for nomor, r in enumerate(daftar, start=1):
        baris = [nomor, r["waktu"]]
        if semua:
            baris.append(r["username"])
        baris += [r["produk"], r["jumlah"], format_rupiah(r["total"])]
        tabel.add_row(baris)
    print(tabel)
    return hitung_total(daftar)




def _header(judul):
    bersihkan_layar()
    print("=" * 60)
    print(judul)
    print("=" * 60)


def menu_utama():
    _header("        TOKO KOMPONEN PC - SISTEM MANAJEMEN")
    tabel = _buat_tabel(["No", "Menu"])
    for baris in [["1", "Login"], ["2", "Register"], ["3", "Keluar"]]:
        tabel.add_row(baris)
    print(tabel)
    return input("Pilih menu: ").strip()


def menu_admin():
    _header(f"  MENU ADMIN  |  Login sebagai: {state['user_aktif']}")
    tabel = _buat_tabel(["No", "Menu"])
    for baris in [
        ["1", "Lihat Semua Produk"], ["2", "Tambah Produk"], ["3", "Ubah Produk"],
        ["4", "Hapus Produk"], ["5", "Cari Produk"], ["6", "Lihat Daftar Pengguna"],
        ["7", "Hapus Pengguna"], ["8", "Riwayat Semua Transaksi"], ["0", "Logout"],
    ]:
        tabel.add_row(baris)
    print(tabel)
    return input("Pilih menu: ").strip()


def menu_pengguna():
    _header(f"  MENU PENGGUNA  |  Login sebagai: {state['user_aktif']}")
    tabel = _buat_tabel(["No", "Menu"])
    for baris in [
        ["1", "Lihat Semua Produk"], ["2", "Cari Produk"], ["3", "Beli Produk"],
        ["4", "Riwayat Pembelian Saya"], ["5", "Ubah Password"], ["0", "Logout"],
    ]:
        tabel.add_row(baris)
    print(tabel)
    return input("Pilih menu: ").strip()
