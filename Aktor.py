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

class Pelanggan(Aktor):
    def __init__(self,id,nama,alamat,email):
        self._id = id
        self._nama = nama
        self._alamat = alamat
        self._email = email

    def getId(self):
        return self._id

    def getNama(self):
        return self._nama

    def getAlamat(self):
        return self._alamat

    def getEmail(self):
        return self._email
