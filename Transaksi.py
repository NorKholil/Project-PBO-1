import Database_Makanan
from Barang import Makanan as makanan
import Database_Kasir
from Aktor import Kasir as kasir
import Database_Pelanggan
from Aktor import Pelanggan as pelanggan
import Database_Elektronik_Revisi
from Barang import Elektronik as elektronik

#x = [(1,2,3),(4,5,6)]

#print(x)
#print(x[0])
#print(x[0][1])
#print(x[1])








kasir = ''

def login(nama):
    kasir = Database_Kasir.melihat_pegawai_dari_nama(nama)
    return kasir

kasir = login('Raisa')

print(kasir)
print(kasir[0][1])






#transaksi = []

#Database_Makanan.melihat_isi_tabel_makanan()
#transaksi.append(Database_Makanan.memasukkan_transaksi_makanan('222333'))
#transaksi.append(Database_Makanan.memasukkan_transaksi_makanan('123456'))
#print(transaksi)
