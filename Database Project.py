import sqlite3
from Aktor import Kasir as kasir

conn = sqlite3.connect("Database Aktor")

c = conn.cursor()

#c.execute("""CREATE TABLE pegawai(id integer primary key, nama text, alamat text) """)



aktor1 = kasir(3, 'Nabila', 'Jember')
aktor2 = kasir(4, 'Raisa', 'Jember')
aktor3 = kasir(5, 'Nadja', 'Jember')

def menambahData(aktor):
    with conn:
        c.execute("INSERT INTO pegawai VALUES (:id, :nama, :alamat)", {'id': aktor._id, 'nama': aktor._nama, 'alamat': aktor._alamat})

#c.execute("INSERT INTO pegawai VALUES ({}, '{}', '{}')".format(aktor1._id, aktor1._nama, aktor1._alamat))

#c.execute("INSERT INTO pegawai VALUES (?, ?, ?)", (aktor2._id, aktor2._nama, aktor2._alamat))

#c.execute("INSERT INTO pegawai VALUES (:id, :nama, :alamat)", {'id': aktor3._id, 'nama': aktor3._nama, 'alamat': aktor3._alamat})
#conn.commit()

c.execute("SELECT * FROM pegawai")
print(c.fetchall())
print(c.fetchone()) 

conn.commit()

conn.close()