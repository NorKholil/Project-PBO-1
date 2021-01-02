import sqlite3
from Aktor import Kasir as kasir

conn = sqlite3.connect("Database Aktor")

c = conn.cursor()

###INI MEMBUAT TABEL###
#c.execute("""CREATE TABLE pegawai(id integer primary key, nama text, alamat text) """)

###INI INSERT MANUAL###
#c.execute("INSERT INTO pegawai VALUES ({}, '{}', '{}')".format(aktor1._id, aktor1._nama, aktor1._alamat))
#c.execute("INSERT INTO pegawai VALUES (?, ?, ?)", (aktor2._id, aktor2._nama, aktor2._alamat))
#c.execute("INSERT INTO pegawai VALUES (:id, :nama, :alamat)", {'id': aktor3._id, 'nama': aktor3._nama, 'alamat': aktor3._alamat})
#conn.commit()

aktor1 = kasir(3, 'Nabila', 'Jember')
aktor2 = kasir(4, 'Raisa', 'Jember')
aktor3 = kasir(5, 'Nadja', 'Jember')
aktor4 = kasir(6, 'Adinda', 'Banyuwangi')
aktor5 = kasir(7, 'Chandra', 'Situbondo')

def menambah_pegawai(pegawai):
    with conn:
        c.execute("INSERT INTO pegawai VALUES (:id, :nama, :alamat)", {'id': pegawai._id, 'nama': pegawai._nama, 'alamat': pegawai._alamat})

def melihat_isi_tabel_pegawai():
    c.execute("SELECT * FROM pegawai")
    print(c.fetchall()) 

def melihat_pegawai_dari_nama(nama):
    c.execute("SELECT * FROM pegawai WHERE nama = :nama", {'nama': nama})
    return c.fetchall()

def update_nama_pegawai(pegawai, nama):
    with conn:
        c.execute("""UPDATE pegawai SET nama = :nama
        WHERE id = :id AND alamat = :alamat""",
        {'id': pegawai._id, 'nama': nama, 'alamat': pegawai._alamat})

def hapus_pegawai(pegawai):
    with conn:
        c.execute("DELETE from pegawai WHERE id = :id",
        {'id': pegawai._id})

conn.commit()

conn.close()
