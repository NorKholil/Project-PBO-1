import sqlite3
from Aktor import Pelanggan as pelanggan

conn = sqlite3.connect("Database XXX")

c = conn.cursor()

###INI MEMBUAT TABEL###
#c.execute("""CREATE TABLE pelanggan(id integer primary key, nama text, alamat text, email text) """)

pelanggan1 = pelanggan(2, 'Rado', 'Jember', 'Rado123@gmail.com')
pelanggan2 = pelanggan(3, 'Radi', 'Jember', 'Radi123@gmail.com')
pelanggan3 = pelanggan(4, 'Radeon', 'Jember', 'Radeon123@gmail.com')
pelanggan4 = pelanggan(5, 'Radiant', 'Jember', 'Radiant123@gmail.com')
pelanggan5 = pelanggan(6, 'Radiance', 'Jember', 'Radiance123@gmail.com')

def menambah_pelanggan(pelanggan):
    with conn:
        c.execute("INSERT INTO pelanggan VALUES (:id, :nama, :alamat, :email)", {'id': pelanggan._id, 'nama': pelanggan._nama, 'alamat': pelanggan._alamat, 'email': pelanggan._email})

def melihat_isi_tabel():
    c.execute("SELECT * FROM pelanggan")
    print(c.fetchall()) 

def melihat_pelanggan_dari_nama(nama):
    c.execute("SELECT * FROM pelanggan WHERE nama = :nama", {'nama': nama})
    return c.fetchall()

def update_nama_pelanggan(pelanggan, nama):
    with conn:
        c.execute("""UPDATE pelanggan SET nama = :nama
        WHERE id = :id AND alamat = :alamat""",
        {'id': pelanggan._id, 'nama': pelanggan._nama, 'alamat': pelanggan._alamat, 'email': pelanggan._email})

def update_alamat_pelanggan(pelanggan, alamat):
    with conn:
        c.execute("""UPDATE pelanggan SET alamat = :alamat
        WHERE id = :id AND nama = :nama""",
        {'id': pelanggan._id, 'nama': pelanggan._nama, 'alamat': pelanggan._alamat, 'email': pelanggan._email})

def update_email_pelanggan(pelanggan, email):
    with conn:
        c.execute("""UPDATE pelanggan SET email = :email
        WHERE id = :id AND alamat = :alamat""",
        {'id': pelanggan._id, 'nama': pelanggan._nama, 'alamat': pelanggan._alamat, 'email': pelanggan._email})

def hapus_pelanggan(pelanggan):
    with conn:
        c.execute("DELETE from pelanggan WHERE id = :id AND nama = :nama",
        {'id': pelanggan._id, 'nama': pelanggan._nama})

conn.commit()

conn.close()