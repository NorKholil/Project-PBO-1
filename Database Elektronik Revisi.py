import sqlite3
from Barang import Elektronik as elektronik

conn = sqlite3.connect("Database XXX")

c = conn.cursor()

###INI MEMBUAT TABEL###
#c.execute("""CREATE TABLE elektronik(nama_barang text, jumlah_barang integer, harga_barang integer, tgl_garansi text, no_seri text primary key) """)

elektronik1 = elektronik('Lenovo Ideapad Slim 3 ARE5', 5, 8500000, '15-02-2022', '12345678')
elektronik2 = elektronik('Lenovo Ideapad Slim 5 ARE3', 4, 9000000, '15-02-2022', '23456781')
elektronik3 = elektronik('Acer Swift Slim 3 ADAG', 5, 8500000, '15-02-2022', '34567812')
elektronik4 = elektronik('ASUS X441U Pro i5 1065G7', 5, 8500000, '15-02-2022', '45678123')
elektronik5 = elektronik('Dell Lattitude i3 8625U', 5, 8500000, '15-02-2022', '56781234')

def menambah_elektronik(elektronik):
    with conn:
        c.execute("INSERT INTO elektronik VALUES (:nama_barang, :jumlah_barang, :harga_barang, :tgl_garansi, :no_seri)", 
        {'nama_barang': elektronik.nama_barang, 'jumlah_barang': elektronik.jumlah_barang, 'harga_barang': elektronik.harga_barang, 'tgl_garansi': elektronik.tgl_garansi, 'no_seri': elektronik.no_seri})

def melihat_isi_tabel_elektronik():
    c.execute("SELECT * FROM elektronik")
    print(c.fetchall()) 

def melihat_elektronik_dari_nama(nama_barang):
    c.execute("SELECT * FROM elektronik WHERE nama_barang = :nama_barang", {'nama_barang': nama_barang})
    return c.fetchall()

def update_nama_elektronik(elektronik, nama_barang):
    with conn:
        c.execute("""UPDATE elektronik SET nama_barang = :nama_barang
        WHERE no_seri = :no_seri""",
        {'nama_barang': nama_barang, 'jumlah_barang': elektronik.jumlah_barang, 'harga_barang': elektronik.harga_barang, 'tgl_garansi': elektronik.tgl_garansi, 'no_seri': elektronik.no_seri})

def update_jumlah_elektronik(elektronik, jumlah_barang):
    with conn:
        c.execute("""UPDATE elektronik SET jumlah_barang = :jumlah_barang
        WHERE no_seri = :no_seri""",
        {'nama_barang': elektronik.nama_barang, 'jumlah_barang': jumlah_barang, 'harga_barang': elektronik.harga_barang, 'tgl_garansi': elektronik.tgl_garansi, 'no_seri': elektronik.no_seri})


def update_harga_elektronik(elektronik, harga_barang):
    with conn:
        c.execute("""UPDATE elektronik SET harga_barang = :harga_barang
        WHERE no_seri = :no_seri""",
        {'nama_barang': elektronik.nama_barang, 'jumlah_barang': elektronik.jumlah_barang, 'harga_barang': harga_barang, 'tgl_garansi': elektronik.tgl_garansi, 'no_seri': elektronik.no_seri})


def update_tgl_garansi_elektronik(elektronik, tgl_garansi):
    with conn:
        c.execute("""UPDATE elektronik SET tgl_garansi = :tgl_garansi
        WHERE no_seri = :no_seri""",
        {'nama_barang': elektronik.nama_barang, 'jumlah_barang': elektronik.jumlah_barang, 'harga_barang': elektronik.harga_barang, 'tgl_garansi': tgl_garansi, 'no_seri': elektronik.no_seri})

def hapus_elektronik(elektronik):
    with conn:
        c.execute("DELETE from elektronik WHERE no_seri = :no_seri",
        {'no_seri': elektronik.no_seri})

conn.commit()

conn.close()
