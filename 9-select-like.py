import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

nama = 'B%'
kursor.execute(f"SELECT * FROM FAUNA WHERE nama_fauna LIKE?", (nama,))
baris_table = kursor.fetchall()

print("Data Fauna Indonesia")
print("="*98)
print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format("id", "nama_fauna","jenis","asal", "jml_skrng", "thn_ditemukan"))
print("="*98)

for baris in baris_table:
    print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format(str(baris[0]),baris[1], baris[2], baris[3], baris[4], baris[5]))
print("="*98)
koneksi.close()