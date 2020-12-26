from abc import ABC, abstractclassmethod

class Aktor(ABC):
    @abstractclassmethod
    def __init__(self,id,nama,alamat):
        pass

    @abstractclassmethod
    def getId(self):
        pass

    @abstractclassmethod
    def getNama(self):
        pass

    @abstractclassmethod
    def getAlamat(self):
        pass

class Kasir(Aktor):
    def __init__(self,id,nama,alamat):
        self._id = id
        self._nama = nama
        self._alamat = alamat

    def getId(self):
        return self._id
    def getNama(self):
        return self._nama

    def getAlamat(self):
        return self._alamat

    def perkenalan(self):
        print("Pelanggan dengan Nomor Id {id}: \nNama saya {nama} dan alamat saya {alamat}".format(
            id = self._id, nama = self._nama, alamat = self._alamat))

class Pelanggan(Aktor):
    def __init__(self,id,nama,alamat,email):
        self._id = id
        self._nama = nama
        self._alamat = alamat
        self.__email = email

    def getId(self):
        return self._id
    def getNama(self):
        return self._nama

    def getAlamat(self):
        return self._alamat

    def perkenalan(self):
        print("Pelanggan dengan Nomor Id {id}:\nNama saya {nama} dan alamat saya {alamat} \nDengan alamat email yaitu {email}".format(
            id = self._id, nama = self._nama, alamat = self._alamat, email = self.__email))


# renanta = Kasir(1920,"Renanta","Jember")
# print(renanta.perkenalan())

renanta = Pelanggan(3241,"Juna","JL. MA.Tamrin 45 Jakarta", "juna123@gamil.com")
print(renanta.perkenalan())