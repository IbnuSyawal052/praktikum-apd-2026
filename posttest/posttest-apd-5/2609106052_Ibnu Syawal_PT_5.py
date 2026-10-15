

# Perintah clear terminal (otomatis menyesuaikan dengan OS pengguna)
import os


perintah_clear = "cls" if os.name == "nt" else "clear"

# DATABASE 

# list user [username, password, role]
users = [
    ["admin", "admin123", "admin"],
    ["user", "user123", "user"],
]

# list produk : [id, nama, kategori, harga, stok]
produk = [
    [1, "Intel Core i5-12400F", "Processor", 2100000, 15],
    [2, "AMD Ryzen 5 5600", "Processor", 1900000, 12],
    [3, "ASUS Prime B660M-K", "Motherboard", 1750000, 8],
    [4, "Corsair Vengeance 16GB DDR4", "RAM", 750000, 20],
    [5, "Samsung 980 NVMe 500GB", "SSD", 850000, 18],
    [6, "NVIDIA RTX 4060 8GB", "VGA", 5500000, 6],
    [7, "Corsair CV650 650W", "PSU", 900000, 10],
]
# untuk menghitung id produk otomatis
id_berikutnya = 8  

# kode riwayat pembelian [username, nama_produk, jumlah, total_harga]
riwayat = []


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
        for u in users:
            if u[0] == username_input and u[1] == password_input:
                user_aktif = u
                break

        if user_aktif is None:
            print("\n[!] Username atau password salah!")
            input("Tekan Enter untuk kembali...")
        else:
            sesi_login = True
            while sesi_login:

                
                #  MENU ADMIN
                
                if user_aktif[2] == "admin":
                    os.system(perintah_clear)
                    print("=" * 60)
                    print(f"  MENU ADMIN  |  Login sebagai: {user_aktif[0]}")
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
                            for p in produk:
                                harga_teks = "Rp" + f"{p[3]:,}".replace(",", ".")
                                print(f"{p[0]:<5}{p[1]:<32}{p[2]:<14}{harga_teks:>14}{p[4]:>7}")
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
                        for p in produk:
                            if p[1].lower() == nama.lower():
                                nama_kembar = True
                                break

                        if nama == "" or kategori == "":
                            print("\n[!] Nama dan kategori tidak boleh kosong!")
                        elif len(nama) > 30:
                            print("\n[!] Nama produk maksimal 30 karakter!")
                        elif len(kategori) > 12:
                            print("\n[!] Kategori maksimal 12 karakter!")
                        elif nama_kembar:
                            print("\n[!] Produk dengan nama tersebut sudah ada!")
                        elif not harga_str.isdigit() or int(harga_str) <= 0:
                            print("\n[!] Harga harus berupa angka bulat lebih dari 0!")
                        elif not stok_str.isdigit():
                            print("\n[!] Stok harus berupa angka bulat (0 atau lebih)!")
                        else:
                            produk.append([id_berikutnya, nama, kategori, int(harga_str), int(stok_str)])
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
                            for p in produk:
                                harga_teks = "Rp" + f"{p[3]:,}".replace(",", ".")
                                print(f"{p[0]:<5}{p[1]:<32}{p[2]:<14}{harga_teks:>14}{p[4]:>7}")

                            id_str = input("\nMasukkan ID produk yang ingin diubah: ").strip()
                            if not id_str.isdigit():
                                print("\n[!] ID harus berupa angka!")
                            else:
                                target = None
                                for p in produk:
                                    if p[0] == int(id_str):
                                        target = p
                                        break

                                if target is None:
                                    print("\n[!] Produk dengan ID tersebut tidak ditemukan!")
                                else:
                                    print("\n(Kosongkan lalu tekan Enter jika tidak ingin mengubah)")
                                    nama_baru = input(f"Nama     [{target[1]}]: ").strip()
                                    kategori_baru = input(f"Kategori [{target[2]}]: ").strip()
                                    harga_baru = input(f"Harga    [{target[3]}]: ").strip()
                                    stok_baru = input(f"Stok     [{target[4]}]: ").strip()

                                    valid = True
                                    if nama_baru != "" and len(nama_baru) > 30:
                                        print("[!] Nama produk maksimal 30 karakter!")
                                        valid = False
                                    if kategori_baru != "" and len(kategori_baru) > 12:
                                        print("[!] Kategori maksimal 12 karakter!")
                                        valid = False
                                    if harga_baru != "" and (not harga_baru.isdigit() or int(harga_baru) <= 0):
                                        print("[!] Harga harus berupa angka bulat lebih dari 0!")
                                        valid = False
                                    if stok_baru != "" and not stok_baru.isdigit():
                                        print("[!] Stok harus berupa angka bulat (0 atau lebih)!")
                                        valid = False

                                    if valid:
                                        if nama_baru != "":
                                            target[1] = nama_baru
                                        if kategori_baru != "":
                                            target[2] = kategori_baru
                                        if harga_baru != "":
                                            target[3] = int(harga_baru)
                                        if stok_baru != "":
                                            target[4] = int(stok_baru)
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
                            for p in produk:
                                harga_teks = "Rp" + f"{p[3]:,}".replace(",", ".")
                                print(f"{p[0]:<5}{p[1]:<32}{p[2]:<14}{harga_teks:>14}{p[4]:>7}")

                            id_str = input("\nMasukkan ID produk yang ingin dihapus: ").strip()
                            if not id_str.isdigit():
                                print("\n[!] ID harus berupa angka!")
                            else:
                                target = None
                                for p in produk:
                                    if p[0] == int(id_str):
                                        target = p
                                        break

                                if target is None:
                                    print("\n[!] Produk dengan ID tersebut tidak ditemukan!")
                                else:
                                    konfirmasi = input(f"Yakin hapus '{target[1]}'? (y/n): ").strip().lower()
                                    if konfirmasi == "y":
                                        produk.remove(target)
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
                            for p in produk:
                                if kata_kunci in p[1].lower() or kata_kunci in p[2].lower():
                                    harga_teks = "Rp" + f"{p[3]:,}".replace(",", ".")
                                    print(f"{p[0]:<5}{p[1]:<32}{p[2]:<14}{harga_teks:>14}{p[4]:>7}")
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
                        for u in users:
                            print(f"{nomor:<5}{u[0]:<20}{'*' * len(u[1]):<15}{u[2]:<10}")
                            nomor += 1
                        input("\nTekan Enter untuk kembali...")

                    # DELETE (hapus pengguna)
                    elif menu == "7":
                        os.system(perintah_clear)
                        print("=== HAPUS PENGGUNA ===")
                        print(f"{'No':<5}{'Username':<20}{'Role':<10}")
                        print("-" * 35)
                        nomor = 1
                        for u in users:
                            print(f"{nomor:<5}{u[0]:<20}{u[2]:<10}")
                            nomor += 1

                        nama_hapus = input("\nMasukkan username yang ingin dihapus: ").strip()
                        target = None
                        for u in users:
                            if u[0] == nama_hapus:
                                target = u
                                break

                        if nama_hapus == "":
                            print("\n[!] Username tidak boleh kosong!")
                        elif target is None:
                            print("\n[!] Username tidak ditemukan!")
                        elif target is user_aktif:
                            print("\n[!] Anda tidak dapat menghapus akun yang sedang digunakan!")
                        else:
                            konfirmasi = input(f"Yakin hapus pengguna '{target[0]}'? (y/n): ").strip().lower()
                            if konfirmasi == "y":
                                users.remove(target)
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
                            for r in riwayat:
                                total_teks = "Rp" + f"{r[3]:,}".replace(",", ".")
                                print(f"{nomor:<5}{r[0]:<15}{r[1]:<32}{r[2]:>5}{total_teks:>16}")
                                total_semua += r[3]
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

                # =====================================================
                #  MENU PENGGUNA BIASA
                # =====================================================
                else:
                    os.system(perintah_clear)
                    print("=" * 60)
                    print(f"  MENU PENGGUNA  |  Login sebagai: {user_aktif[0]}")
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
                            for p in produk:
                                harga_teks = "Rp" + f"{p[3]:,}".replace(",", ".")
                                print(f"{p[0]:<5}{p[1]:<32}{p[2]:<14}{harga_teks:>14}{p[4]:>7}")
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
                            for p in produk:
                                if kata_kunci in p[1].lower() or kata_kunci in p[2].lower():
                                    harga_teks = "Rp" + f"{p[3]:,}".replace(",", ".")
                                    print(f"{p[0]:<5}{p[1]:<32}{p[2]:<14}{harga_teks:>14}{p[4]:>7}")
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
                            for p in produk:
                                harga_teks = "Rp" + f"{p[3]:,}".replace(",", ".")
                                print(f"{p[0]:<5}{p[1]:<32}{p[2]:<14}{harga_teks:>14}{p[4]:>7}")

                            id_str = input("\nMasukkan ID produk yang ingin dibeli: ").strip()
                            if not id_str.isdigit():
                                print("\n[!] ID harus berupa angka!")
                            else:
                                target = None
                                for p in produk:
                                    if p[0] == int(id_str):
                                        target = p
                                        break

                                if target is None:
                                    print("\n[!] Produk dengan ID tersebut tidak ditemukan!")
                                elif target[4] == 0:
                                    print("\n[!] Maaf, stok produk ini sedang habis!")
                                else:
                                    print(f"\nProduk : {target[1]}")
                                    print(f"Harga  : Rp{target[3]:,}".replace(",", "."))
                                    print(f"Stok   : {target[4]}")
                                    jumlah_str = input("Jumlah beli: ").strip()

                                    if not jumlah_str.isdigit() or int(jumlah_str) <= 0:
                                        print("\n[!] Jumlah harus berupa angka bulat lebih dari 0!")
                                    elif int(jumlah_str) > target[4]:
                                        print(f"\n[!] Stok tidak cukup! Stok tersedia: {target[4]}")
                                    else:
                                        jumlah = int(jumlah_str)
                                        total = jumlah * target[3]
                                        total_teks = f"Rp{total:,}".replace(",", ".")
                                        konfirmasi = input(f"Total bayar {total_teks}. Lanjutkan? (y/n): ").strip().lower()
                                        if konfirmasi == "y":
                                            target[4] -= jumlah
                                            riwayat.append([user_aktif[0], target[1], jumlah, total])
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
                        for r in riwayat:
                            if r[0] == user_aktif[0]:
                                if nomor == 1:
                                    print(f"{'No':<5}{'Produk':<32}{'Jml':>5}{'Total':>16}")
                                    print("-" * 58)
                                total_teks = "Rp" + f"{r[3]:,}".replace(",", ".")
                                print(f"{nomor:<5}{r[1]:<32}{r[2]:>5}{total_teks:>16}")
                                total_belanja += r[3]
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

                        if pass_lama != user_aktif[1]:
                            print("\n[!] Password lama salah!")
                        elif len(pass_baru) < 6:
                            print("\n[!] Password baru minimal 6 karakter!")
                        elif " " in pass_baru:
                            print("\n[!] Password tidak boleh mengandung spasi!")
                        elif pass_baru != pass_konfirmasi:
                            print("\n[!] Konfirmasi password tidak cocok!")
                        else:
                            user_aktif[1] = pass_baru
                            print("\n[+] Password berhasil diubah.")
                        input("Tekan Enter untuk kembali...")

                    #  LOGOUT ----------
                    elif menu == "0":
                        sesi_login = False

                    else:
                        print("\n[!] Menu tidak valid! Pilih angka 0 - 5.")
                        input("Tekan Enter untuk melanjutkan...")


    # REGISTER (akun baru otomatis berperan sebagai pengguna biasa)

    elif pilihan == "2":
        os.system(perintah_clear)
        print("=== REGISTER AKUN BARU ===")
        username_baru = input("Username (min 4 karakter, tanpa spasi) : ").strip()
        password_baru = input("Password (min 6 karakter, tanpa spasi) : ").strip()
        password_ulang = input("Konfirmasi password                    : ").strip()

        username_dipakai = False
        for u in users:
            if u[0].lower() == username_baru.lower():
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
            users.append([username_baru, password_baru, "user"])
            print(f"\n[+] Registrasi berhasil! Silakan login sebagai '{username_baru}'.")
        input("Tekan Enter untuk kembali...")


    # KELUAR

    elif pilihan == "3":
        os.system(perintah_clear)
        print("Terima kasih telah menggunakan sistem Toko Komponen PC!")
        program_berjalan = False

    else:
        print("\n[!] Menu tidak valid! Pilih angka 1 - 3.")
        input("Tekan Enter untuk melanjutkan...")