class motor:
    def __init__ (self, cc, warna, tahun, nama, merk):
        self.cc    = cc
        self.warna = warna
        self.tahun = tahun
        self.nama  = nama
        self.merk  = merk
    
    def printname(self):
        print(self.cc)
        print(self.warna)
        print(self.tahun)
        print(self.nama)
        print(self.merk)

class manual(motor):
    def __init__(self, cc, warna, tahun, nama, merk):
        motor.__init__(self, cc, warna, tahun, nama,  merk)
        self.bahanbakar = "Pertamax"

    def MotManual(self):
        print("Bahan bakar : ", self.bahanbakar)
        print("CC          : ", self.cc)
        print("Warna       : ", self.warna)
        print("Tahun       : ", self.tahun)
        print("Nama        : ", self.nama)
        print("Merk        : ", self.merk)

class otomatis(motor):
    def __init__(self, cc, warna, tahun, nama, merk):
        motor.__init__(self, cc, warna, tahun, nama, merk)
        self.bahanbakar = "Pertalite"

    def MotMatic(self):
        print("Bahan Bakar  : ", self.bahanbakar)
        print("CC           : ", self.cc)
        print("Warna        : ", self.warna)
        print("Tahun        : ", self.tahun)
        print("Nama         : ", self.nama)
        print("Merk         : ", self.merk)

x = manual("150cc", "Merah", 2019, "CBR150", "Honda")
y = otomatis("250cc", "Hitam", 2020, "XMax", "Yamaha")

x.MotManual()
y.MotMatic()