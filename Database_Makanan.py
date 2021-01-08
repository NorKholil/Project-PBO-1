import sqlite3
from Barang import Makanan as makanan

conn = sqlite3.connect("Database Makanan")

c = conn.cursor()

###INI MEMBUAT TABEL###
# c.execute("""CREATE TABLE makanan(nama_barang text, jumlah_barang integer, harga_barang integer, nomor_barcode primary key, tgl_expired text) """)


makanan1 = makanan('Oreo', 2, 10000, '222333', '12-10-2021')
makanan2 = makanan('Chitos', 3, 15500, '444332', '12-11-2021')
makanan3 = makanan('Siver Quen', 3, 20000, '223344', '12-12-2021')
makanan4 = makanan('Dove', 4 , 25000, '554466', '8-10-2021')
makanan5 = makanan('Tanggo', 5 , 17000, '3344553', '12-9-2021')

def menambah_makanan(makanan):
    conn = sqlite3.connect("Database Makanan")

    c = conn.cursor()

    with conn:
        c.execute("INSERT INTO makanan VALUES (:nama_barang, :jumlah_barang, :harga_barang, :nomor_barcode, :tgl_expired)", {'nama_barang': makanan.nama_barang, 'jumlah_barang': makanan.jumlah_barang, 'harga_barang': makanan.harga_barang, 'nomor_barcode': makanan.nomor_barcode, 'tgl_expired': makanan.tgl_expired})


def melihat_isi_tabel_makanan():
    conn = sqlite3.connect("Database Makanan")

    c = conn.cursor()

    c.execute("SELECT * FROM makanan")
    print(c.fetchall()) 


def melihat_makanan_berdasarkan_nama(nama_barang):
    conn = sqlite3.connect("Database Makanan")

    c = conn.cursor()

    c.execute("SELECT * FROM makanan WHERE nama_barang = :nama_barang", {'nama_barang': nama_barang})
    return c.fetchall()


def update_nama_makanan(makanan, nama_barang):
    conn = sqlite3.connect("Database Makanan")

    c = conn.cursor()

    with conn:
        c.execute("""UPDATE makanan SET nama_barang = :nama_barang
        WHERE nomor_barcode = :nomor_barcode""",
        {'nama_barang': nama_barang, 'jumlah_barang': makanan.jumlah_barang, 'harga_barang': makanan.harga_barang, 'nomor_barcode': makanan.nomor_barcode, 'tgl_expired': makanan.tgl_expired})


def update_jumlah_makanan(makanan, jumlah_barang):
    conn = sqlite3.connect("Database Makanan")

    c = conn.cursor()

    with conn:
        c.execute("""UPDATE makanan SET jumlah_barang = :jumlah_barang
        WHERE nomor_barcode = :nomor_barcode""",
        {'nama_barang': makanan.nama_barang, 'jumlah_barang': jumlah_barang, 'harga_barang': makanan.harga_barang, 'nomor_barcode': makanan.nomor_barcode, 'tgl_expired': makanan.tgl_expired})


def update_harga_makanan(makanan, harga_barang):
    conn = sqlite3.connect("Database Makanan")

    c = conn.cursor()

    with conn:
        c.execute("""UPDATE makanan SET harga_barang = :harga_barang
        WHERE nomor_barcode = :nomor_barcode""",
        {'nama_barang': makanan.nama_barang, 'jumlah_barang': makanan.jumlah_barang, 'harga_barang': harga_barang, 'nomor_barcode': makanan.nomor_barcode, 'tgl_expired': makanan.tgl_expired})


def update_tgl_expired_makanan(makanan, tgl_expired):
    conn = sqlite3.connect("Database Makanan")

    c = conn.cursor()

    with conn:
        c.execute("""UPDATE makanan SET tgl_expired = :tgl_expired
        WHERE nomor_barcode = :nomor_barcode""",
        {'nama_barang': makanan.nama_barang, 'jumlah_barang': makanan.jumlah_barang, 'harga_barang': makanan.harga_barang, 'nomor_barcode': makanan.nomor_barcode, 'tgl_expired': tgl_expired})


def hapus_makanan(makanan):
    conn = sqlite3.connect("Database Makanan")

    c = conn.cursor()

    with conn:
        c.execute("DELETE from makanan WHERE nomor_barcode = :nomor_barcode",
        {'nomor_barcode': makanan.nomor_barcode})


def memasukkan_transaksi_makanan(nomor_barcode):
    temp = []

    conn = sqlite3.connect("Database Makanan")

    c = conn.cursor()
    
    c.execute("SELECT * FROM makanan WHERE nomor_barcode = :nomor_barcode", {'nomor_barcode': nomor_barcode})
    temp.append(c.fetchall())
    return temp


conn.commit()

conn.close()