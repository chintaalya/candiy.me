class produk:
    def __init__(self, nama, jenis, stok, terjual):
        self.__nama = nama
        self.__jenis = jenis
        self.__stok = stok
        self.__terjual = terjual

    def getNama(self):
        return self.__nama

    def getJenis(self):
        return self.__jenis

    def getStok(self):
        return self.__stok

    def getTerjual(self):
        return self.__terjual

class moneyin:
    def __init__(self, tanggal, keterangan, nominal):
        self.__tanggal = tanggal
        self.__keterangan = keterangan
        self.__nominal = nominal

    def getTanggal(self):
        return self.__tanggal

    def getKeterangan(self):
        return self.__keterangan

    def getNominal(self):
        return self.__nominal

class moneyout:
    def __init__(self, tanggal, keterangan, nominal):
        self.__tanggal = tanggal
        self.__keterangan = keterangan
        self.__nominal = nominal

    def getTanggal(self):
        return self.__tanggal

    def getKeterangan(self):
        return self.__keterangan

    def getNominal(self):
        return self.__nominal