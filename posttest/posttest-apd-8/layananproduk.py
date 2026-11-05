"""Fitur produk: lihat, tambah, ubah, hapus, cari."""
from database import produk, daftar_kategori, state
from tampilantabel import tampil_tabel_produk
from halhalberguna import bersihkan_layar, tekan_enter, ubah_ke_angka


def cari_produk(kata_kunci):
    hasil = {}
    for id_p, p in produk.items():
        if kata_kunci in p["nama"].lower() or kata_kunci in p["kategori"].lower():
            hasil[id_p] = p
    return hasil


def lihat_produk():
    bersihkan_layar()
    print("=== DAFTAR PRODUK ===")
    tampil_tabel_produk(produk)
    tekan_enter()


def tambah_produk():
    bersihkan_layar()
    print("=== TAMBAH PRODUK ===")
    try:
        nama = input("Nama produk  : ").strip()
        kategori = input(f"Kategori ({', '.join(daftar_kategori)}) : ").strip()
        harga_str = input("Harga (Rp)   : ").strip()
        stok_str = input("Stok         : ").strip()

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
        id_baru = state["id_produk"]
        produk[id_baru] = {"nama": nama, "kategori": kategori, "harga": harga, "stok": stok}
        print(f"\n[+] Produk '{nama}' berhasil ditambahkan dengan ID {id_baru}.")
        state["id_produk"] += 1
    finally:
        tekan_enter()


def ubah_produk():
    bersihkan_layar()
    print("=== UBAH PRODUK ===")
    try:
        if len(produk) == 0:
            raise ValueError("Belum ada produk.")
        tampil_tabel_produk(produk)

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
        tekan_enter()


def hapus_produk():
    bersihkan_layar()
    print("=== HAPUS PRODUK ===")
    try:
        if len(produk) == 0:
            raise ValueError("Belum ada produk.")
        tampil_tabel_produk(produk)

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
        tekan_enter()


def menu_cari_produk():
    bersihkan_layar()
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
            tampil_tabel_produk(hasil)
            print(f"\n{len(hasil)} produk ditemukan.")
    finally:
        tekan_enter()
