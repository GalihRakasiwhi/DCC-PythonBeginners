#1. buat 1 buah class parrent apapun dengan minimal 2 atribut
#2. buat 1 buah class child dari class parrent anda

class HP:
    def __init__(self, merek = None, tipe = None):
        self.merek = merek
        self.tipe = tipe

    def getMerek(self):
        return self.merek

    def getTipe(self):
        return self.tipe

class Realme(HP):
    def __init__(self, model = None, warna = None):
        self.model = model
        self.warna = warna

    def getModel(self):
        return self.model

    def getWarna(self):
        return self.warna

hpRealme = Realme("3 Pro", "Ocean Blue")
hpRealme.merek = "Realme"
hpRealme.tipe = "Flagship"
print(hpRealme.merek)
print(hpRealme.getModel())
print(hpRealme.getWarna())
print(hpRealme.tipe)
print(f"HP saya merek \"{hpRealme.merek}\", dengan type \"{hpRealme.getModel()}\", warnanya \"{hpRealme.getWarna()}\" bentuknya \"{hpRealme.tipe}\"")
