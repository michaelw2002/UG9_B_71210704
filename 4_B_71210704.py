print("=====GEBYAR DISKON=====")
print("=====MASUKKAN JUMLAH BARANG YANG DIPESAN=====")
kipas_angin = int(input("KIPAS ANGIN DISKON 10% Rp 25.000,00 : "))
sepeda      = int(input("SEPEDA DISKON 55%      Rp 6.000,00  : "))
helm_rossi  = int(input("HELM ROSSI DISKON 77%  Rp 8.000,00  : "))

#perhitungan
jumlah_diskon_kipas = 25000 * kipas_angin * 10 / 100
jumlah_diskon_sepeda = 6000 * sepeda * 55 / 100
jumlah_diskon_helm = 8000 * helm_rossi * 77 / 100
jumlah_total_diskon = jumlah_diskon_kipas + jumlah_diskon_sepeda + jumlah_diskon_helm

#total
print("=====TOTAL=====")
print("TOTAL KIPAS ANGIN : ",jumlah_diskon_kipas)
print("TOTAL SEPEDA : ",jumlah_diskon_sepeda)
print("TOTAL HELM ROSSI : ",jumlah_diskon_helm)
print("Jumlah total diskon yang didapat adalah Rp",jumlah_total_diskon)
