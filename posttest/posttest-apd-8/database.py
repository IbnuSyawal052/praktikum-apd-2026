import hashlib


def hash_password(password):
    # password disimpan dalam bentuk hash SHA-256, bukan teks asli
    return hashlib.sha256(password.encode()).hexdigest()


# dictionary user {username: {"password": hash, "role": }}
users = {
    "admin": {"password": hash_password("admin123"), "role": "admin"},
    "user": {"password": hash_password("user123"), "role": "user"},
}

# dictionary produk {id: {"nama": , "kategori": , "harga": , "stok": }}
produk = {
    1: {"nama": "Intel Core i5-12400F", "kategori": "Processor", "harga": 2100000, "stok": 15},
    2: {"nama": "AMD Ryzen 5 5600", "kategori": "Processor", "harga": 1900000, "stok": 12},
    3: {"nama": "ASUS Prime B660M-K", "kategori": "Motherboard", "harga": 1750000, "stok": 8},
    4: {"nama": "Corsair Vengeance 16GB DDR4", "kategori": "RAM", "harga": 750000, "stok": 20},
    5: {"nama": "Samsung 980 NVMe 500GB", "kategori": "SSD", "harga": 850000, "stok": 18},
    6: {"nama": "NVIDIA RTX 4060 8GB", "kategori": "VGA", "harga": 5500000, "stok": 6},
    7: {"nama": "Corsair CV650 650W", "kategori": "PSU", "harga": 900000, "stok": 10},
}

# riwayat pembelian {id: {"waktu": , "username": , "produk": , "jumlah": , "total": }}
riwayat = {}

# daftar kategori yang boleh dipakai
daftar_kategori = ["Processor", "GPU", "RAM", "SSD", "Motherboard", "VGA", "PSU"]

# state program. Disimpan dalam dictionary agar bisa diubah dari file lain
# (variabel biasa yang di-import tidak ikut berubah jika diubah di file lain)
state = {
    "user_aktif": None,    # username yang sedang login (None = belum login)
    "id_produk": 8,        # id produk berikutnya
    "id_riwayat": 1,       # id riwayat berikutnya
}
