import Database_Makanan
from Barang import Makanan as makanan
import Database_Kasir
from Aktor import Kasir as kasir
import Database_Pelanggan
from Aktor import Pelanggan as pelanggan
import Database_Elektronik_Revisi
from Barang import Elektronik as elektronik



def menampilkanMenu():
    print('|----------------------------------------|')
    print('Pilih menu:')
    print('1. Input Transaksi')
    print('2. Mengubah Transaksi')
    print('3. Melihat Data Barang')
    print('4. Melihat Data Harga Barang')
    print('5. Melihat Data Pelanggan')
    print('6. Menambah Data Pelanggan')
    print('7. Mengubah Data Pelanggan')
    print('|----------------------------------------|')

    pilihan = str (input('Masukkan pilihan: '))
    if pilihan == "3" :
        print("---Data Makanan---\n")
        print(Database_Makanan.melihat_isi_tabel_makanan())
        print("---Data Elektronik---\n")
        print(Database_Elektronik_Revisi.melihat_isi_tabel_elektronik())

    if pilihan == "4" :
        print("|---------------------------------|")
        print("Lihat Data Harga:")
        print("1. Makanan")
        print("2. Elektronik")
        print("|---------------------------------|")
        pilihan = str (input('Masukkan pilihan: '))
        if pilihan == "1" :
            harga = ''
            def melihatHarga(nama):
                harga = Database_Makanan.melihat_makanan_berdasarkan_nama(nama)
                return harga

            harga = melihatHarga(str(input("Maksukkan Nama Makanan:")))
            print(harga[0][2])

        else :
            harga = ''
            def melihatHarga(nama):
                harga = Database_Elektronik_Revisi.melihat_elektronik_dari_nama(nama)
                return harga
            harga = melihatHarga(str(input("Maksukkan Nama Makanan:")))
            print(harga[0][2])

    if pilihan == '5':
        data_Pelanggan = Database_Pelanggan.melihat_pelanggan_dari_nama(input("Masukkan nama: "))
        print(data_Pelanggan)

    if pilihan == '6':
        Database_Pelanggan.melihat_isi_tabel_pelanggan()
        temp = pelanggan(input("Masukkan id: "),input("Masukkan nama: "),input("Masukkan alamat: "),input("Masukkan email: "))
        Database_Pelanggan.menambah_pelanggan(temp)
        Database_Pelanggan.melihat_isi_tabel_pelanggan()

    if pilihan == '7':

        temp = ""
        Database_Pelanggan.melihat_isi_tabel_pelanggan()
        temp = Database_Pelanggan.melihat_pelanggan_dari_nama(input("Masukkan nama pelanggan: "))
        print(temp)

        print("""1. Mengubah nama pelanggan\n
        2. Mengubah alamat pelanggan\n
        3. Mengubah email pelanggan""")

        pilihan = str(input("Masukkan pilihan: "))        
        
        if pilihan == "1":
            Database_Pelanggan.update_nama_pelanggan(temp,input("Masukkan nama baru: "))
        if pilihan == "2":
            Database_Pelanggan.update_nama_pelanggan(temp,input("Masukkan alamat baru: "))
        if pilihan == "3":
            Database_Pelanggan.update_nama_pelanggan(temp,input("Masukkan email baru: "))
        else:
            print("Pilihan salah")

menampilkanMenu()