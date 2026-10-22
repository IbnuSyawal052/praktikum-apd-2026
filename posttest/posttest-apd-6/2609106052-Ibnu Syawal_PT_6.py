# Perintah clear terminal (otomatis menyesuaikan dengan OS pengguna)
import os


perintah_clear = "cls" if os.name == "nt" else "clear"

# DATABASE

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

# kode riwayat pembelian [username, nama_produk, jumlah, total_harga]
riwayat = {}
# untuk menghitung id riwayat otomatis
id_riwayat = 1


# PROGRAM UTAMA

program_berjalan = True
while program_berjalan:
    os.system(perintah_clear)
    print("=" * 60)
    print("        TOKO KOMPONEN PC - SISTEM MANAJEMEN")
    print("=" * 60)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("-" * 60)
    pilihan = input("Pilih menu: ").strip()

    # LOGIN

    if pilihan == "1":
        os.system(perintah_clear)
        print("=== LOGIN ===")
        username_input = input("Username : ").strip()
        password_input = input("Password : ").strip()

        user_aktif = None
        if username_input in users and users[username_input]["password"] == password_input:
            user_aktif = username_input

        if user_aktif is None:
            print("\n[!] Username atau password salah!")
            input("Tekan Enter untuk kembali...")
        else:
            sesi_login = True
            while sesi_login:


                #  MENU ADMIN

                if users[user_aktif]["role"] == "admin":
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
                    menu = input("Pilih menu: ").strip()

                    # READ (lihat semua produk)
                    if menu == "1":
                        os.system(perintah_clear)
                        print("=== DAFTAR PRODUK ===")
                        if len(produk) == 0:
                            print("Belum ada produk.")
                        else:
                            print(f"{'ID':<5}{'Nama':<32}{'Kategori':<14}{'Harga':>14}{'Stok':>7}")
                            print("-" * 72)
                            for id_p, p in produk.items():
                                harga_teks = "Rp" + f"{p['harga']:,}".replace(",", ".")
                                print(f"{id_p:<5}{p['nama']:<32}{p['kategori']:<14}{harga_teks:>14}{p['stok']:>7}")
                        input("\nTekan Enter untuk kembali...")

                    #  CREATE (tambah produk)
                    elif menu == "2":
                        os.system(perintah_clear)
                        print("=== TAMBAH PRODUK ===")
                        nama = input("Nama produk  : ").strip()
                        kategori = input("Kategori (Processor, GPU, RAM, SSD, Motherboard, VGA, PSU)    : ").strip()
                        harga_str = input("Harga (Rp)                      : ").strip()
                        stok_str = input("Stok                            : ").strip()

                        nama_kembar = False
                        for p in produk.values():
                            if p["nama"].lower() == nama.lower():
                                nama_kembar = True
                                break

                        if nama == "" or kategori == "":
                            print("\n[!] Nama dan kategori tidak boleh kosong!")
                        elif len(nama) > 30:
                            print("\n[!] Nama produk maksimal 30 karakter!")
                        elif kategori not in ["Processor", "GPU", "RAM", "SSD", "Motherboard", "VGA", "PSU"]:
                            print("\n[!] Kategori tidak terdaftar!")
                        elif nama_kembar:
                            print("\n[!] Produk dengan nama tersebut sudah ada!")
                        elif not harga_str.isdigit() or int(harga_str) <= 0:
                            print("\n[!] Harga harus berupa angka bulat lebih dari 0!")
                        elif not stok_str.isdigit():
                            print("\n[!] Stok harus berupa angka bulat (0 atau lebih)!")
                        else:
                            produk[id_berikutnya] = {
                                "nama": nama,
                                "kategori": kategori,
                                "harga": int(harga_str),
                                "stok": int(stok_str),
                            }
                            print(f"\n[+] Produk '{nama}' berhasil ditambahkan dengan ID {id_berikutnya}.")
                            id_berikutnya += 1
                        input("Tekan Enter untuk kembali...")

                    #  UPDATE (ubah produk)

                    elif menu == "3":
                        os.system(perintah_clear)
                        print("=== UBAH PRODUK ===")
                        if len(produk) == 0:
                            print("Belum ada produk.")
                        else:
                            print(f"{'ID':<5}{'Nama':<32}{'Kategori':<14}{'Harga':>14}{'Stok':>7}")
                            print("-" * 72)
                            for id_p, p in produk.items():
                                harga_teks = "Rp" + f"{p['harga']:,}".replace(",", ".")
                                print(f"{id_p:<5}{p['nama']:<32}{p['kategori']:<14}{harga_teks:>14}{p['stok']:>7}")

                            id_str = input("\nMasukkan ID produk yang ingin diubah: ").strip()
                            if not id_str.isdigit():
                                print("\n[!] ID harus berupa angka!")
                            else:
                                target = None
                                if int(id_str) in produk:
                                    target = produk[int(id_str)]

                                if target is None:
                                    print("\n[!] Produk dengan ID tersebut tidak ditemukan!")
                                else:
                                    print("\n(Kosongkan lalu tekan Enter jika tidak ingin mengubah)")
                                    nama_baru = input(f"Nama     [{target['nama']}]: ").strip()
                                    kategori_baru = input(f"Kategori [{target['kategori']}]: ").strip()
                                    harga_baru = input(f"Harga    [{target['harga']}]: ").strip()
                                    stok_baru = input(f"Stok     [{target['stok']}]: ").strip()

                                    valid = True
                                    if nama_baru != "" and len(nama_baru) > 30:
                                        print("[!] Nama produk maksimal 30 karakter!")
                                        valid = False
                                    if kategori_baru != "" and kategori_baru not in ["Processor", "GPU", "RAM", "SSD", "Motherboard", "VGA", "PSU"]:
                                        print("[!] Kategori tidak terdaftar!")
                                        valid = False
                                    if harga_baru != "" and (not harga_baru.isdigit() or int(harga_baru) <= 0):
                                        print("[!] Harga harus berupa angka bulat lebih dari 0!")
                                        valid = False
                                    if stok_baru != "" and not stok_baru.isdigit():
                                        print("[!] Stok harus berupa angka bulat (0 atau lebih)!")
                                        valid = False

                                    if valid:
                                        if nama_baru != "":
                                            target["nama"] = nama_baru
                                        if kategori_baru != "":
                                            target["kategori"] = kategori_baru
                                        if harga_baru != "":
                                            target["harga"] = int(harga_baru)
                                        if stok_baru != "":
                                            target["stok"] = int(stok_baru)
                                        print("\n[+] Produk berhasil diperbarui.")
                                    else:
                                        print("\n[!] Perubahan dibatalkan karena ada input yang tidak valid.")
                        input("Tekan Enter untuk kembali...")

                    #  DELETE (hapus produk)
                    elif menu == "4":
                        os.system(perintah_clear)
                        print("=== HAPUS PRODUK ===")
                        if len(produk) == 0:
                            print("Belum ada produk.")
                        else:
                            print(f"{'ID':<5}{'Nama':<32}{'Kategori':<14}{'Harga':>14}{'Stok':>7}")
                            print("-" * 72)
                            for id_p, p in produk.items():
                                harga_teks = "Rp" + f"{p['harga']:,}".replace(",", ".")
                                print(f"{id_p:<5}{p['nama']:<32}{p['kategori']:<14}{harga_teks:>14}{p['stok']:>7}")

                            id_str = input("\nMasukkan ID produk yang ingin dihapus: ").strip()
                            if not id_str.isdigit():
                                print("\n[!] ID harus berupa angka!")
                            else:
                                if int(id_str) not in produk:
                                    print("\n[!] Produk dengan ID tersebut tidak ditemukan!")
                                else:
                                    target = produk[int(id_str)]
                                    konfirmasi = input(f"Yakin hapus '{target['nama']}'? (y/n): ").strip().lower()
                                    if konfirmasi == "y":
                                        del produk[int(id_str)]
                                        print("\n[+] Produk berhasil dihapus.")
                                    else:
                                        print("\n[i] Penghapusan dibatalkan.")
                        input("Tekan Enter untuk kembali...")

                    # READ (cari produk)
                    elif menu == "5":
                        os.system(perintah_clear)
                        print("=== CARI PRODUK ===")
                        kata_kunci = input("Masukkan nama / kategori produk: ").strip().lower()
                        if kata_kunci == "":
                            print("\n[!] Kata kunci tidak boleh kosong!")
                        else:
                            ditemukan = 0
                            print(f"\n{'ID':<5}{'Nama':<32}{'Kategori':<14}{'Harga':>14}{'Stok':>7}")
                            print("-" * 72)
                            for id_p, p in produk.items():
                                if kata_kunci in p["nama"].lower() or kata_kunci in p["kategori"].lower():
                                    harga_teks = "Rp" + f"{p['harga']:,}".replace(",", ".")
                                    print(f"{id_p:<5}{p['nama']:<32}{p['kategori']:<14}{harga_teks:>14}{p['stok']:>7}")
                                    ditemukan += 1
                            if ditemukan == 0:
                                print("Produk tidak ditemukan.")
                            else:
                                print(f"\n{ditemukan} produk ditemukan.")
                        input("\nTekan Enter untuk kembali...")

                    # READ (daftar pengguna)
                    elif menu == "6":
                        os.system(perintah_clear)
                        print("=== DAFTAR PENGGUNA ===")
                        print(f"{'No':<5}{'Username':<20}{'Password':<15}{'Role':<10}")
                        print("-" * 50)
                        nomor = 1
                        for nama_user, data_user in users.items():
                            print(f"{nomor:<5}{nama_user:<20}{'*' * len(data_user['password']):<15}{data_user['role']:<10}")
                            nomor += 1
                        input("\nTekan Enter untuk kembali...")

                    # DELETE (hapus pengguna)
                    elif menu == "7":
                        os.system(perintah_clear)
                        print("=== HAPUS PENGGUNA ===")
                        print(f"{'No':<5}{'Username':<20}{'Role':<10}")
                        print("-" * 35)
                        nomor = 1
                        for nama_user, data_user in users.items():
                            print(f"{nomor:<5}{nama_user:<20}{data_user['role']:<10}")
                            nomor += 1

                        nama_hapus = input("\nMasukkan username yang ingin dihapus: ").strip()

                        if nama_hapus == "":
                            print("\n[!] Username tidak boleh kosong!")
                        elif nama_hapus not in users:
                            print("\n[!] Username tidak ditemukan!")
                        elif nama_hapus == user_aktif:
                            print("\n[!] Anda tidak dapat menghapus akun yang sedang digunakan!")
                        else:
                            konfirmasi = input(f"Yakin hapus pengguna '{nama_hapus}'? (y/n): ").strip().lower()
                            if konfirmasi == "y":
                                del users[nama_hapus]
                                print("\n[+] Pengguna berhasil dihapus.")
                            else:
                                print("\n[i] Penghapusan dibatalkan.")
                        input("Tekan Enter untuk kembali...")

                    #  READ (semua riwayat transaksi)
                    elif menu == "8":
                        os.system(perintah_clear)
                        print("=== RIWAYAT SEMUA TRANSAKSI ===")
                        if len(riwayat) == 0:
                            print("Belum ada transaksi.")
                        else:
                            print(f"{'No':<5}{'Pembeli':<15}{'Produk':<32}{'Jml':>5}{'Total':>16}")
                            print("-" * 73)
                            nomor = 1
                            total_semua = 0
                            for r in riwayat.values():
                                total_teks = "Rp" + f"{r['total']:,}".replace(",", ".")
                                print(f"{nomor:<5}{r['username']:<15}{r['produk']:<32}{r['jumlah']:>5}{total_teks:>16}")
                                total_semua += r["total"]
                                nomor += 1
                            print("-" * 73)
                            print(f"Total pendapatan: Rp{total_semua:,}".replace(",", "."))
                        input("\nTekan Enter untuk kembali...")

                    #  LOGOUT ----------
                    elif menu == "0":
                        sesi_login = False

                    else:
                        print("\n[!] Menu tidak valid! Pilih angka 0 - 8.")
                        input("Tekan Enter untuk melanjutkan...")


                #  MENU PENGGUNA BIASA

                else:
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
                    menu = input("Pilih menu: ").strip()

                    #  READ (lihat produk)
                    if menu == "1":
                        os.system(perintah_clear)
                        print("=== DAFTAR PRODUK ===")
                        if len(produk) == 0:
                            print("Belum ada produk.")
                        else:
                            print(f"{'ID':<5}{'Nama':<32}{'Kategori':<14}{'Harga':>14}{'Stok':>7}")
                            print("-" * 72)
                            for id_p, p in produk.items():
                                harga_teks = "Rp" + f"{p['harga']:,}".replace(",", ".")
                                print(f"{id_p:<5}{p['nama']:<32}{p['kategori']:<14}{harga_teks:>14}{p['stok']:>7}")
                        input("\nTekan Enter untuk kembali...")

                    #  READ (cari produk)
                    elif menu == "2":
                        os.system(perintah_clear)
                        print("=== CARI PRODUK ===")
                        kata_kunci = input("Masukkan nama / kategori produk: ").strip().lower()
                        if kata_kunci =="":
                            print("\n[!] Kata kunci tidak boleh kosong!")
                        else:
                            ditemukan = 0
                            print(f"\n{'ID':<5}{'Nama':<32}{'Kategori':<14}{'Harga':>14}{'Stok':>7}")
                            print("-" * 72)
                            for id_p, p in produk.items():
                                if kata_kunci in p["nama"].lower() or kata_kunci in p["kategori"].lower():
                                    harga_teks = "Rp" + f"{p['harga']:,}".replace(",", ".")
                                    print(f"{id_p:<5}{p['nama']:<32}{p['kategori']:<14}{harga_teks:>14}{p['stok']:>7}")
                                    ditemukan += 1
                            if ditemukan == 0:
                                print("Produk tidak ditemukan.")
                            else:
                                print(f"\n{ditemukan} produk ditemukan.")
                        input("\nTekan Enter untuk kembali...")

                    #  Beli produk (mengurangi stok)
                    elif menu == "3":
                        os.system(perintah_clear)
                        print("=== BELI PRODUK ===")
                        if len(produk) == 0:
                            print("Belum ada produk.")
                        else:
                            print(f"{'ID':<5}{'Nama':<32}{'Kategori':<14}{'Harga':>14}{'Stok':>7}")
                            print("-" * 72)
                            for id_p, p in produk.items():
                                harga_teks = "Rp" + f"{p['harga']:,}".replace(",", ".")
                                print(f"{id_p:<5}{p['nama']:<32}{p['kategori']:<14}{harga_teks:>14}{p['stok']:>7}")

                            id_str = input("\nMasukkan ID produk yang ingin dibeli: ").strip()
                            if not id_str.isdigit():
                                print("\n[!] ID harus berupa angka!")
                            else:
                                target = None
                                if int(id_str) in produk:
                                    target = produk[int(id_str)]

                                if target is None:
                                    print("\n[!] Produk dengan ID tersebut tidak ditemukan!")
                                elif target["stok"] == 0:
                                    print("\n[!] Maaf, stok produk ini sedang habis!")
                                else:
                                    print(f"\nProduk : {target['nama']}")
                                    print(f"Harga  : Rp{target['harga']:,}".replace(",", "."))
                                    print(f"Stok   : {target['stok']}")
                                    jumlah_str = input("Jumlah beli: ").strip()

                                    if not jumlah_str.isdigit() or int(jumlah_str) <= 0:
                                        print("\n[!] Jumlah harus berupa angka bulat lebih dari 0!")
                                    elif int(jumlah_str) > target["stok"]:
                                        print(f"\n[!] Stok tidak cukup! Stok tersedia: {target['stok']}")
                                    else:
                                        jumlah = int(jumlah_str)
                                        total = jumlah * target["harga"]
                                        total_teks = f"Rp{total:,}".replace(",", ".")
                                        konfirmasi = input(f"Total bayar {total_teks}. Lanjutkan? (y/n): ").strip().lower()
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
                        input("Tekan Enter untuk kembali...")

                    #  READ (riwayat pembelian milik sendiri)
                    elif menu == "4":
                        os.system(perintah_clear)
                        print("=== RIWAYAT PEMBELIAN SAYA ===")
                        nomor = 1
                        total_belanja = 0
                        for r in riwayat.values():
                            if r["username"] == user_aktif:
                                if nomor == 1:
                                    print(f"{'No':<5}{'Produk':<32}{'Jml':>5}{'Total':>16}")
                                    print("-" * 58)
                                total_teks = "Rp" + f"{r['total']:,}".replace(",", ".")
                                print(f"{nomor:<5}{r['produk']:<32}{r['jumlah']:>5}{total_teks:>16}")
                                total_belanja += r["total"]
                                nomor += 1
                        if nomor == 1:
                            print("Anda belum pernah melakukan pembelian.")
                        else:
                            print("-" * 58)
                            print(f"Total belanja: Rp{total_belanja:,}".replace(",", "."))
                        input("\nTekan Enter untuk kembali...")

                    #  UPDATE (untuk mengubah password sendiri)
                    elif menu == "5":
                        os.system(perintah_clear)
                        print("=== UBAH PASSWORD ===")
                        pass_lama = input("Password lama          : ").strip()
                        pass_baru = input("Password baru          : ").strip()
                        pass_konfirmasi = input("Konfirmasi password   : ").strip()

                        if pass_lama != users[user_aktif]["password"]:
                            print("\n[!] Password lama salah!")
                        elif len(pass_baru) < 6:
                            print("\n[!] Password baru minimal 6 karakter!")
                        elif " " in pass_baru:
                            print("\n[!] Password tidak boleh mengandung spasi!")
                        elif pass_baru != pass_konfirmasi:
                            print("\n[!] Konfirmasi password tidak cocok!")
                        else:
                            users[user_aktif]["password"] = pass_baru
                            print("\n[+] Password berhasil diubah.")
                        input("Tekan Enter untuk kembali...")

                    #  LOGOUT ----------
                    elif menu == "0":
                        sesi_login = False

                    else:
                        print("\n[!] Menu tidak valid! Pilih angka 0 - 5.")
                        input("Tekan Enter untuk melanjutkan...")


    # REGISTER (akun baru otomatis akan diberi role pengguna biasa)

    elif pilihan == "2":
        os.system(perintah_clear)
        print("=== REGISTER AKUN BARU ===")
        username_baru = input("Username (min 4 karakter, tanpa spasi) : ").strip()
        password_baru = input("Password (min 6 karakter, tanpa spasi) : ").strip()
        password_ulang = input("Konfirmasi password                    : ").strip()

        username_dipakai = False
        for nama_user in users:
            if nama_user.lower() == username_baru.lower():
                username_dipakai = True
                break

        if len(username_baru) < 4:
            print("\n[!] Username minimal 4 karakter!")
        elif " " in username_baru:
            print("\n[!] Username tidak boleh mengandung spasi!")
        elif username_dipakai:
            print("\n[!] Username sudah digunakan, silakan pilih yang lain!")
        elif len(password_baru) < 6:
            print("\n[!] Password minimal 6 karakter!")
        elif " " in password_baru:
            print("\n[!] Password tidak boleh mengandung spasi!")
        elif password_baru != password_ulang:
            print("\n[!] Konfirmasi password tidak cocok!")
        else:
            users[username_baru] = {"password": password_baru, "role": "user"}
            print(f"\n[+] Registrasi berhasil! Silakan login sebagai '{username_baru}'.")
        input("Tekan Enter untuk kembali...")


    # KELUAR

    elif pilihan == "3":
        os.system(perintah_clear)
        print("Terima kasih telah menggunakan sistem ini. Sampai jumpa!")
        program_berjalan = False

    else:
        print("\n[!] Menu tidak valid! Pilih angka 1 - 3.")
        input("Tekan Enter untuk melanjutkan...")