# Konfigurasi Akun
USERNAME_SAYA = "Ibnu Syawal" 
PASSWORD_SAYA = "052"         

# Variabel penampung total luas lahan (dalam Hektare)
total_kalimantan_gambut = 0
total_kalimantan_mineral = 0
total_sumatera_gambut = 0
total_sumatera_mineral = 0

# Form Login
login_berhasil = False

while not login_berhasil:
    print("=" * 55)
    print("   SISTEM REKAPITULASI TITIK API - BPBD & MANGGALA AGNI")
    print("=" * 55)
    
    # Menerima input dan menghapus spasi berlebih atau tidak sengaja dengan .strip()
    input_user = input("Masukkan Username : ").strip()
    input_pass = input("Masukkan Password : ").strip()
    
    # Penanganan Input Kosong 
    if input_user == "" or input_pass == "":
        print("[!] Kesalahan: Username dan Password tidak boleh kosong!\n")
        continue

    # Kode untuk men detect jika hanya salah satu yang salah 
    if input_user.lower() == USERNAME_SAYA.lower() and input_pass == PASSWORD_SAYA:
        print("\n[+] Login Berhasil! Selamat datang, {}.".format(USERNAME_SAYA))
        login_berhasil = True
    elif input_user.lower() == USERNAME_SAYA.lower():
        print("[!] Kesalahan: Password yang Anda masukkan salah.\n")
    elif input_pass == PASSWORD_SAYA:
        print("[!] Kesalahan: Username yang Anda masukkan salah.\n")
    else:
        print("[!] Kesalahan: Username dan Password salah.\n")

# 
lanjut_input = "Y"

while lanjut_input.upper() == "Y":
    print("\n" + "-" * 55)
    print("                  INPUT DATA LOKASI")
    print("-" * 55)
    
    # Input Wilayah Pulau
    pulau = ""
    while pulau == "":
        pulau = input("Masukkan Wilayah (KALIMANTAN / SUMATERA) : ").strip().upper()
        if pulau == "":
            print("   -> Input wilayah tidak boleh kosong!")
        elif pulau != "KALIMANTAN" and pulau != "SUMATERA":
            print("   -> Wilayah tidak valid! Harap masukkan Kalimantan atau Sumatera.")
            pulau = "" 
            
    # Input Jenis Lahan 
    lahan = ""
    while lahan == "":
        if pulau == "KALIMANTAN" or pulau == "SUMATERA": 
            lahan = input("Masukkan Jenis Lahan (GAMBUT / MINERAL)  : ").strip().upper()
            
            if lahan == "":
                print("   -> Input lahan tidak boleh kosong!")
            elif lahan != "GAMBUT" and lahan != "MINERAL":
                print("   -> Lahan tidak valid! Harap masukkan Gambut atau Mineral.")
                lahan = "" 
                
    # Input untuk jumlah hotspot
    hotspot_valid = False
    hotspot = 0
    while not hotspot_valid:
        input_hotspot = input("Masukkan Jumlah Titik Api (Hotspot)      : ").strip()
        
        if input_hotspot == "":
            print("   -> Jumlah titik api tidak boleh kosong!")
        elif not input_hotspot.isdigit():
            print("   -> Harap masukkan angka bulat yang valid!")
        else:
            hotspot = int(input_hotspot)
            hotspot_valid = True
            
    # Kode untuk konversi
    luas_rusak = hotspot * 5
    print(f"\n[INFO] {pulau}-{lahan}: {hotspot} Titik Api berdampak pada {luas_rusak} Hektare lahan.")
    
    # Menambahkan data ke variabel kategori masing-masing 
    if pulau == "KALIMANTAN":
        if lahan == "GAMBUT":
            total_kalimantan_gambut += luas_rusak
        elif lahan == "MINERAL":
            total_kalimantan_mineral += luas_rusak
    elif pulau == "SUMATERA":
        if lahan == "GAMBUT":
            total_sumatera_gambut += luas_rusak
        elif lahan == "MINERAL":
            total_sumatera_mineral += luas_rusak

    # Konfirmasi pengulangan input Y/T
    tanya_valid = False
    while not tanya_valid:
        tanya = input("\nApakah anda masih mau input data titik api lagi? (Y/T): ").strip().upper()
        if tanya == "":
            print("   -> Pilihan tidak boleh kosong!")
        elif tanya == "Y" or tanya == "T":
            lanjut_input = tanya
            tanya_valid = True
        else:
            print("   -> Masukkan huruf Y untuk lanjut atau T untuk berhenti.")

# Output nya
print("\n" + "=" * 55)
print("     RINGKASAN KERUSAKAN LAHAN - SATELIT BMKG")
print("=" * 55)
print(f" 1. Kalimantan - Gambut  : {total_kalimantan_gambut} Hektare")
print(f" 2. Kalimantan - Mineral : {total_kalimantan_mineral} Hektare")
print(f" 3. Sumatera - Gambut    : {total_sumatera_gambut} Hektare")
print(f" 4. Sumatera - Mineral   : {total_sumatera_mineral} Hektare")
print("=" * 55)
print("Data telah diteruskan ke pusat.")