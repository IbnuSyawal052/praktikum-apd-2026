from getpass import getpass

from database import users, state, hash_password
from halhalberguna import bersihkan_layar, tekan_enter


def login():
    bersihkan_layar()
    print("=== LOGIN ===")
    username_input = input("Username : ").strip()
    password_input = getpass("Password : ").strip()
    try:
        if (username_input not in users
                or users[username_input]["password"] != hash_password(password_input)):
            raise ValueError("Username atau password salah!")
    except ValueError as e:
        print(f"\n[!] {e}")
        tekan_enter()
    else:
        state["user_aktif"] = username_input


def register():
    # akun baru otomatis diberi role pengguna biasa
    bersihkan_layar()
    print("=== REGISTER AKUN BARU ===")
    username_baru = input("Username (min 4 karakter, tanpa spasi) : ").strip()
    password_baru = getpass("Password (min 6 karakter, tanpa spasi) : ").strip()
    password_ulang = getpass("Konfirmasi password                    : ").strip()
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
        users[username_baru] = {"password": hash_password(password_baru), "role": "user"}
        print(f"\n[+] Registrasi berhasil! Silakan login sebagai '{username_baru}'.")
    finally:
        tekan_enter()


def ubah_password():
    bersihkan_layar()
    print("=== UBAH PASSWORD ===")
    pass_lama = getpass("Password lama          : ").strip()
    pass_baru = getpass("Password baru          : ").strip()
    pass_konfirmasi = getpass("Konfirmasi password   : ").strip()
    user = state["user_aktif"]
    try:
        if hash_password(pass_lama) != users[user]["password"]:
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
        users[user]["password"] = hash_password(pass_baru)
        print("\n[+] Password berhasil diubah.")
    finally:
        tekan_enter()
