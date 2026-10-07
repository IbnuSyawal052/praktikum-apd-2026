# formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
# print (formula1[4][0])

# sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# print(sirkuit)

# sirkuit.append("Keter")
# sirkuit.extend(["Keter", "Hokma", "Binah", "Geburah"])
# sirkuit.insert(3, "Chesed")
# sirkuit[4] = "Tiphereth"
# sirkuit[0:3] = ["Keter", "Hokma", "Binah"]
# del sirkuit[3]
# sirkuit.remove("Keter")
# print(sirkuit)
# ambil_sirkuit = sirkuit.pop(0)
# print(ambil_sirkuit)
# Sephirah = ["Keter", "Hokma", "Binah", "Geburah", "Chesed",
# "Tiphereth", "Netzach", "Hod", "Yesod", "Malkuth"]
# print(Sephirah[0:6:2])
# Lower_Floor_Sephirah = ["Hod", "Yesod", "Malkuth"]
#     print(Lower_Floor_Sephirah)
# Middle_Floor_Sephirah = ["Geburah", "Chesed", "Tiphereth", "Netzach"]
#     print(Middle_Floor_Sephirah)
# Upper_Floor_Sephirah = ["Keter", "Hokma", "Binah"]
#     print(Upper_Floor_Sephirah)

# Sephirah = Upper_Floor_Sephirah + Middle_Floor_Sephirah + Lower_Floor_Sephirah
#     print(Sephirah)
# juara_WDC = ["MacLaren", "Red Bull"]
# juara = juara_WDC * 3
# print(juara)

# line_up = [
# ["Ferrari", "Leclerc", 16],
# ["Mercedes", "Hamilton", 44],
# ["Red Bull", "Verstappen", 1],
# ["McLaren", "Norris", 4]
# ]
# # print(line_up[2][1])
# for i in line_up:
#     for j in i:
#         print(j)

# chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# list_chara = list(chara)
# # list_chara.append("Reimu")
# input_baru = input("Masukkan character baru: ")
# list_chara.extend(input_baru.split(","))
# chara = tuple(list_chara)
# print(chara)

# print(chara[2])
# print(chara[-1])
# print(chara[4][0])

# chara = ("Yukari", "Yukino", "Odette", "Senku", "Amamiya Ren", "Sparkle", "Herta", "Asta", "Arlan")
# (Persona, Oregairu, Genshin, DrStone, Persona5, StarRail, *SpaceStation) = chara
# print(Persona5)
# print(SpaceStation)

# data_harian = ["Senin", 36.5, "Selasa", 37.1, "Rabu", 36.8, "Kamis", 37.0, "Jumat", 36.6, "Sabtu", 36.9, "Minggu", 37.2]


# suhu_saja = data_harian[1::2]

# print("Angka suhu untuk grafik:", suhu_saja)
import math

# =====================================================================
# DATABASE ITEM MOBILE LEGENDS (Item Populer yang Memengaruhi Damage/DEF)
# =====================================================================
ATTACK_ITEMS = {
    "blade of despair": {"flat_pen": 0, "pct_pen": 0.0, "desc": "+160 Physical Attack (+25% jika HP target < 50%)"},
    "malefic roar": {"flat_pen": 0, "pct_pen": 0.20, "desc": "+20% Physical PEN (Pasif: Tambah %PEN sesuai DEF musuh)"},
    "hunter strike": {"flat_pen": 15, "pct_pen": 0.0, "desc": "+15 Flat Physical PEN, +80 Physical Attack"},
    "blade of the heptaseas": {"flat_pen": 15, "pct_pen": 0.0, "desc": "+15 Flat Physical PEN, +70 Physical Attack"},
    "fury hammer": {"flat_pen": 12, "pct_pen": 0.0, "desc": "+12 Flat Physical PEN (Item Tier 2)"}
}

MAGIC_ITEMS = {
    "holy crystal": {"flat_pen": 0, "pct_pen": 0.0, "flat_red": 0, "desc": "+100 Magic Power (+Persentase Magic Power)"},
    "divine glaive": {"flat_pen": 0, "pct_pen": 0.40, "flat_red": 0, "desc": "+40% Magic PEN (Pasif: Tambah %PEN jika DEF musuh tinggi)"},
    "genius wand": {"flat_pen": 10, "pct_pen": 0.0, "flat_red": 27, "desc": "+10 Flat Magic PEN (Pasif: Mengurangi hingga 27 Flat DEF musuh)"},
    "arcane boots": {"flat_pen": 10, "pct_pen": 0.0, "flat_red": 0, "desc": "+10 Flat Magic PEN (Sepatu)"}
}

DEFENSE_ITEMS = {
    "antique cuirass": {"dmg_red": 0.18, "desc": "Mengurangi hingga 18% Physical Attack musuh setelah terkena skill"},
    "athena shield": {"dmg_red": 0.25, "desc": "Mengurangi 25% Magic Damage yang diterima selama 3-5 detik pertama"},
    "radiant armor": {"dmg_red": 0.20, "desc": "Mengurangi Magic Damage flat per-stack (estimasi reduksi efektif ~20%)"},
    "blade armor": {"dmg_red": 0.0, "desc": "+90 Physical Defense & Memantulkan Basic Attack"},
    "dominance ice": {"dmg_red": 0.0, "desc": "+70 Physical Defense & Mengurangi Attack Speed/Regen musuh"}
}

# =====================================================================
# FUNGSI UTAMA KALKULASI DAMAGE
# =====================================================================
def hitung_actual_damage(gross_damage, base_def, flat_red=0, pct_red=0, pct_pen=0, flat_pen=0, dmg_reduction_pct=0):
    # 1. Hitung Adjusted DEF (Wajib Berurutan sesuai Aturan MLBB)
    adjusted_def = base_def - flat_red
    adjusted_def = adjusted_def * (1 - pct_red)
    adjusted_def = adjusted_def * (1 - pct_pen)
    adjusted_def = adjusted_def - flat_pen
    
    # Batas minimum DEF di MLBB adalah -60
    if adjusted_def < -60:
        adjusted_def = -60
        
    # 2. Hitung Faktor Pengurang DEF (120 / (120 + DEF))
    if adjusted_def >= 0:
        damage_after_def = gross_damage * (120 / (120 + adjusted_def))
    else:
        # Jika DEF minus, damage yang masuk justru meningkat (Maksimal 2x lipat)
        damage_after_def = gross_damage * (2 - (120 / (120 - adjusted_def)))
        
    # 3. Hitung Akhir dipotong Persentase Damage Reduction musuh
    actual_damage = damage_after_def * (1 - dmg_reduction_pct)
    
    return round(actual_damage), round(adjusted_def)

# =====================================================================
# MENU INTERAKTIF INPUT BARANG
# =====================================================================
def main():
    print("==================================================")
    print("   WELCOME TO MLBB INTERACTIVE DAMAGE CALCULATOR  ")
    print("==================================================")
    
    # 1. Pilih Tipe Serangan
    tipe_damage = input("Tipe Damage Serangan? (physical / magic): ").strip().lower()
    while tipe_damage not in ["physical", "magic"]:
        tipe_damage = input("Mohon ketik 'physical' atau 'magic': ").strip().lower()

    # 2. Input Status Dasar
    try:
        gross_dmg = float(input("\nMasukkan Gross Damage (Damage Mentah Skill/Hit): "))
        base_def = float(input("Masukkan DEF Awal Target (Physical/Magic Defense Musuh): "))
    except ValueError:
        print("Input harus berupa angka! Program terhenti.")
        return

    # Inisialisasi Modifier Stat dari Item
    flat_pen = 0
    pct_pen = 0.0
    flat_red = 0
    dmg_red = 0.0

    # Tampilkan database item yang relevan ke user
    db_pilihan = ATTACK_ITEMS if tipe_damage == "physical" else MAGIC_ITEMS
    print(f"\n--- DAFTAR ITEM {tipe_damage.upper()} YANG TERSEDIA ---")
    for nama, detail in db_pilihan.items():
        print(f"- {nama.title()} ({detail['desc']})")

    # 3. Input Barang Penyerang
    print("\n[INPUT BARANG PENYERANG]")
    print("Ketik nama item dari daftar di atas (Ketik 'done' jika sudah selesai memilih):")
    while True:
        item_input = input("-> Masukkan nama item: ").strip().lower()
        if item_input == "done":
            break
        elif item_input in db_pilihan:
            flat_pen += db_pilihan[item_input].get("flat_pen", 0)
            pct_pen += db_pilihan[item_input].get("pct_pen", 0.0)
            flat_red += db_pilihan[item_input].get("flat_red", 0)
            print(f"   [Berhasil Ditambahkan] {item_input.title()}")
        else:
            print("   [Peringatan] Nama item tidak ditemukan dalam daftar, coba lagi.")

    # Tampilkan database item defense ke user
    print(f"\n--- DAFTAR ITEM DEFENSE YANG TERSEDIA ---")
    for nama, detail in DEFENSE_ITEMS.items():
        print(f"- {nama.title()} ({detail['desc']})")

    # 4. Input Barang Target (Musuh)
    print("\n[INPUT BARANG TARGET / MUSUH]")
    print("Ketik nama item defense di atas (Ketik 'done' jika sudah selesai memilih):")
    while True:
        item_input = input("-> Masukkan nama item defense: ").strip().lower()
        if item_input == "done":
            break
        elif item_input in DEFENSE_ITEMS:
            dmg_red += DEFENSE_ITEMS[item_input].get("dmg_red", 0.0)
            print(f"   [Berhasil Ditambahkan] {item_input.title()}")
        else:
            print("   [Peringatan] Nama item tidak ditemukan dalam daftar, coba lagi.")

    # 5. Eksekusi Perhitungan Rumus MLBB
    final_dmg, final_def = hitung_actual_damage(
        gross_damage=gross_dmg,
        base_def=base_def,
        flat_red=flat_red,
        pct_red=0,  # Dapat ditambahkan jika memperhitungkan pasif skill hero spesifik
        pct_pen=pct_pen,
        flat_pen=flat_pen,
        dmg_reduction_pct=dmg_red
    )

    # 6. Output Hasil Akhir
    print("\n==================================================")
    print("               HASIL KALKULASI AKHIR              ")
    print("==================================================")
    print(f"Tipe Serangan                  : {tipe_damage.upper()}")
    print(f"Gross Damage awal              : {gross_dmg}")
    print(f"DEF Awal Target                : {base_def}")
    print(f"Total Penetrasi Diakumulasi   : Flat PEN: {flat_pen} | % PEN: {int(pct_pen*100)}%")
    print(f"Total Reduksi Damage Target    : {int(dmg_red*100)}%")
    print(f"--------------------------------------------------")
    print(f"DEF AKHIR TARGET SETELAH PEN   : {final_def}")
    print(f"💥 DAMAGE NYATA YANG DITERIMA MUSUH : {final_dmg} HP 💥")
    print("==================================================")

if __name__ == "__main__":
    main()
