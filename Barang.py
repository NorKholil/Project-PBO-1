class Barang:
    def __init__(self,nama_barang,jumlah_barang,harga_barang):
        self.nama_barang = nama_barang
        self.jumlah_barang = jumlah_barang
        self.harga_barang = harga_barang
    
    def setnama_barang(self, value):
        self.nama_barang = value

    def setjumlah_barang(self, value):
        self.jumlah_barang = value

    def setharga_barang(self, value):
        self.harga_barang = value

    def getnama_barang(self) :
        return self.nama_barang 

    def getjumlah_barang(self) :
        return self.jumlah_barang 
    
    def getharga_barang(self) :
        return self.harga_barang

    def tampilkanData(self):
        print("Nama Barang :", self.nama_barang)
        print("Jumlah Barang :", self.jumlah_barang)
        print("Harga Barang :", self.harga_barang)

class Eletronik(Barang):
    def __init__(self, nama_barang, jumlah_barang, harga_barang, tgl_garansi, no_seri):
        super().__init__(nama_barang,jumlah_barang,harga_barang)
        self.tgl_garansi = tgl_garansi
        self.no_seri = no_seri

    def tampilkanData(self):
        print("Nama Barang :", self.nama_barang)
        print("Jumlah Barang :", self.jumlah_barang)
        print("Harga Barang :", self.harga_barang)
        print("Tanggal Garansi :", self.tgl_garansi)
        print("Nomor Seri :", self.no_seri)
        

class Makanan(Barang):
    def __init__(self, nama_barang, jumlah_barang, harga_barang, nomor_Barcode, tgl_Expired):
        super().__init__(nama_barang,jumlah_barang,harga_barang)
        self.nomor_barcode = nomor_Barcode
        self.tgl_expired = tgl_Expired

    def tampilkanData(self, seri):
        self.seri = seri
        if seri == "-":
            print("Nomor Barcode :", self.nomor_barcode)
            print("Nama Barang :", self.nama_barang)
            print("Jumlah Barang :", self.jumlah_barang)
            print("Harga Barang :", self.harga_barang)
            print("Tanggal Expired :", self.tgl_expired)
        else:
            print("Nomor Barcode :", self.nomor_barcode)
            print("Nama Barang :", self.nama_barang)
            print("Jumlah Barang :", self.jumlah_barang)
            print("Harga Barang :", self.harga_barang)
            print("Tanggal Expired :", self.tgl_expired)
            print("No Seri :", self.seri)
