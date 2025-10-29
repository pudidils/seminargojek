# Program Klasifikasi Usia

# 1. TODO: Baca input dari pengguna
awal = int(input("umur: "))
# 2. TODO Tentukan kategori berdasarkan usia
usia = "Lansia" if awal >= 60 else "Dewasa" if awal >= 18 else "Remaja" if awal >= 12 else "Bocil"
print("Kategori: ", usia)
