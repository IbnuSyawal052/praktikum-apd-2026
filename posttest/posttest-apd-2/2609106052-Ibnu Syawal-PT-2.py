


makanan_1 = 15000
makanan_2 = 16000
makanan_3 = 19000
makanan_4 = 20000
makanan_5 = 21000
makanan_6 = 22000

harga_makanan = [makanan_1, makanan_2, makanan_3, makanan_4, makanan_5, makanan_6]
biaya_aplikasi = 5000

total_harga_makanan = (
    makanan_1
    + makanan_2
    + makanan_3
    + makanan_4
    + makanan_5
    + makanan_6
)
total_bayar = total_harga_makanan + biaya_aplikasi

rata_rata = total_bayar / len(harga_makanan)
nim = 52      
bolean = nim != rata_rata

kurs_euro = 20535
mata_uang_euro = total_bayar / kurs_euro


print("harga_makanan:", harga_makanan)
print("biaya_aplikasi:", biaya_aplikasi)
print("total_bayar:", total_bayar)
print("rata_rata:", rata_rata)
print("bolean (nim != rata_rata):", bolean)
print("mata_uang_euro:", mata_uang_euro)
print("harga_makanan[-6:]   :", harga_makanan[-6:])   
