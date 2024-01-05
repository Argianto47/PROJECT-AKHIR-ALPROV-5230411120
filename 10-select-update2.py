import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

id_fauna_baru = 4
asal_baru = 'Kalimantan Timur'
kursor.execute(f"UPDATE FAUNA SET asal = '{asal_baru}' WHERE id_fauna = {id_fauna_baru}")
koneksi.commit()

if kursor.rowcount > 0:
    print(f"Data Dengan ID {id_fauna_baru} Berhasil Diubah!")

koneksi.close()

