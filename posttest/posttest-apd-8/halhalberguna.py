import os


def bersihkan_layar():
    # otomatis menyesuaikan dengan OS pengguna
    os.system("cls" if os.name == "nt" else "clear")


def tekan_enter(pesan="Tekan Enter untuk kembali..."):
    input(f"\n{pesan}")


def format_rupiah(angka):
    return "Rp" + f"{angka:,}".replace(",", ".")


def ubah_ke_angka(teks, nama_field, minimal):
    # mengubah input ke integer, kalau gagal akan memunculkan error
    try:
        angka = int(teks)
    except ValueError:
        raise ValueError(f"{nama_field} harus berupa angka bulat!")
    if angka < minimal:
        raise ValueError(f"{nama_field} minimal {minimal}!")
    return angka


def hitung_total(daftar, i=0):
    # REKURSIF: daftar = list transaksi, i = index yang sedang dihitung
    if i == len(daftar):
        return 0
    return daftar[i]["total"] + hitung_total(daftar, i + 1)
