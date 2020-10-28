"""
Buat class menghitung luas bangun
Segitiga > luas & keliling

rumus luas : 1/2 x a x t
rumus keliling : sisi + sisi + sisi
"""
"""
class BangunDatar:
    def __init__(self, a=None, b=None, c=None, t=None, p=None, l=None):
        self.a = a
        self.b = b
        self.c = c
        self.t = t
        self.p = p
        self.l = l

    def getLuasSegitiga(self):
        print(0.5 * self.a * self.t)
    def getKelilingSegitiga(self):
        print(self.a + self.b + self.c)

    def getLuasPP(self):
        print(self.p * self.l)
    def getKelilingPP(self):
        print((2*self.p) + (2*self.l))

print("\nSegitiga: ")
luasSegitiga = BangunDatar(a=5, t=5)
luasSegitiga.getLuasSegitiga()
kelilingSegitiga = BangunDatar(a=5, b=3, c=5)
kelilingSegitiga.getKelilingSegitiga()
print("\nPersegi Panjang: ")
luasPP = BangunDatar(p=10, l=5)
luasPP.getLuasPP()
kelilingPP = BangunDatar(p=10, l=5)
kelilingPP.getKelilingPP()
"""
"""
data = [
    {
        "nama": "Luke Skywalker",
        "jabatan": "Jedi Master"
    }
]
"""
"""
data = []
record = {}
record["nama"] = "Luke Skywalker"
record["jabatan"] = "Jedi Masater"
data.append(record)

for x in data:
    print(x)
"""

class SaveData:
    def __init__(self):
        self.record = []

    def save(self, nama=None, jabatan=None):
        self.record.append({"nama": nama, "jabatan": jabatan})
        print(self.record)

    def getData(self):
        for x in data:
            print(x)

listData = SaveData()
listData.save(nama="John Doe", jabatan="Knight")
