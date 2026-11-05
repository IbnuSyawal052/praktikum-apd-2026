"""Fitur manajemen pengguna (khusus admin)."""
from database import users, state
from tampilantabel import tampil_tabel_pengguna
from halhalberguna import bersihkan_layar, tekan_enter


def lihat_pengguna():
    bersihkan_layar()
    print("=== DAFTAR PENGGUNA ===")
    tampil_tabel_pengguna()
    tekan_enter()


def hapus_pengguna():
    bersihkan_layar()
    print("=== HAPUS PENGGUNA ===")
    tampil_tabel_pengguna(sembunyikan_password=False)

    try:
        nama_hapus = input("\nMasukkan username yang ingin dihapus: ").strip()
        if nama_hapus == "":
            raise ValueError("Username tidak boleh kosong!")
        if nama_hapus == state["user_aktif"]:
            raise ValueError("Anda tidak dapat menghapus akun yang sedang digunakan!")
        users[nama_hapus]  # memicu KeyError jika tidak ada
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
        tekan_enter()
