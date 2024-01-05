import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

id_fauna_baru = 10
jumlah_baru = 650
kursor.execute(f"UPDATE FAUNA SET jml_skrng = {jumlah_baru} WHERE id_fauna = {id_fauna_baru}")
koneksi.commit()

if kursor.rowcount > 0:
    print(f"Data Dengan ID {id_fauna_baru} Berhasil Diubah!")

koneksi.close()