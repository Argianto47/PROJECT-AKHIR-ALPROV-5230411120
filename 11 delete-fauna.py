import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

asal = 'Kalimantan' 
kursor.execute(f"DELETE FROM FAUNA WHERE asal = ?", (asal,))
koneksi.commit()

if kursor.rowcount > 0: 
    print(f"Data Dengan Asal {asal} Berhasil Diubah!")

koneksi.close()