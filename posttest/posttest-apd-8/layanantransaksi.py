from datetime import datetime

from database import produk, riwayat, state
from tampilantabel import tampil_tabel_produk, tampil_tabel_riwayat
from halhalberguna import bersihkan_layar, tekan_enter, ubah_ke_angka, format_rupiah


def beli_produk():
    bersihkan_layar()
    print("=== BELI PRODUK ===")
    try:
        if len(produk) == 0:
            raise ValueError("Belum ada produk.")
        tampil_tabel_produk(produk)

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
            riwayat[state["id_riwayat"]] = {
                "waktu": datetime.now().strftime("%d-%m-%Y %H:%M"),
                "username": state["user_aktif"],
                "produk": target["nama"],
                "jumlah": jumlah,
                "total": total,
            }
            state["id_riwayat"] += 1
            print("\n[+] Pembelian berhasil! Terima kasih.")
        else:
            print("\n[i] Pembelian dibatalkan.")
    finally:
        tekan_enter()


def riwayat_semua():
    bersihkan_layar()
    print("=== RIWAYAT SEMUA TRANSAKSI ===")
    try:
        if len(riwayat) == 0:
            raise ValueError("Belum ada transaksi.")
        total = tampil_tabel_riwayat(list(riwayat.values()), semua=True)
        print(f"Total pendapatan: {format_rupiah(total)}")
    except ValueError as e:
        print(e)
    finally:
        tekan_enter()


def riwayat_saya():
    bersihkan_layar()
    print("=== RIWAYAT PEMBELIAN SAYA ===")
    milik_sendiri = [r for r in riwayat.values() if r["username"] == state["user_aktif"]]
    try:
        if len(milik_sendiri) == 0:
            raise ValueError("Anda belum pernah melakukan pembelian.")
        total = tampil_tabel_riwayat(milik_sendiri, semua=False)
        print(f"Total belanja: {format_rupiah(total)}")
    except ValueError as e:
        print(e)
    finally:
        tekan_enter()
