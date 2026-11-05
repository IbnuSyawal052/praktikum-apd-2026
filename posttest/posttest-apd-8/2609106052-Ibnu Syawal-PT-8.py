from database import users, state
from tampilantabel import menu_utama, menu_admin, menu_pengguna
from halhalberguna import bersihkan_layar, tekan_enter
from loginygy import login, register, ubah_password
from layananproduk import (lihat_produk, tambah_produk, ubah_produk, hapus_produk, menu_cari_produk)
from admincekuser import lihat_pengguna, hapus_pengguna
from layanantransaksi import beli_produk, riwayat_semua, riwayat_saya


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
            tekan_enter("Tekan Enter untuk melanjutkan...")


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
            tekan_enter("Tekan Enter untuk melanjutkan...")


def main():
    program_berjalan = True
    while program_berjalan:
        pilihan = menu_utama()

        if pilihan == "1":
            login()
            if state["user_aktif"] is not None:
                if users[state["user_aktif"]]["role"] == "admin":
                    sesi_admin()
                else:
                    sesi_pengguna()
                state["user_aktif"] = None

        elif pilihan == "2":
            register()

        elif pilihan == "3":
            bersihkan_layar()
            print("Terima kasih telah menggunakan sistem ini. Sampai jumpa!")
            program_berjalan = False

        else:
            print("\n[!] Menu tidak valid! Pilih angka 1 - 3.")
            tekan_enter("Tekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    main()