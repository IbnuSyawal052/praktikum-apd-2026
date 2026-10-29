from autentikasi import login
from mahasiswa import tambah_mahasiswa, lihat_mahasiswa

print("=== Selamat Datang di Sistem Akademik ===")

# Menggunakan fungsi dari modul autentikasi
if login("admin", "123"):
    print("Login berhasil!\n")
# Menggunakan fungsi dari modul mahasiswa
    tambah_mahasiswa("Budi Santoso", "2609106010")
    tambah_mahasiswa("Siti Aminah", "2609106011")
    lihat_mahasiswa()
else:
    print("Login gagal! Username atau password salah.")