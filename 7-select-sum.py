import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

kursor.execute("SELECT SUM(jml_skrng) FROM FAUNA")
rata_rata_fauna = kursor.fetchone()[0]

print(f"Total Populasi Fauna Indonesia:",(rata_rata_fauna))

koneksi.close()