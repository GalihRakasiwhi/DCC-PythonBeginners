#solve code kang chandra
"""
#first class
class Cemilan(object):
    def __init__(self, nama=None, bahan=None):
        self.nama = nama
        self.bahan = bahan

    def namaCemilan(self):
        return self.nama
    
    def bahanCemilan(self):
        return self.bahan

#second class
class Rasa(Cemilan):

    def __init__(self, rasa=None, tekstur=None):
        self.rasa = rasa
        self.tekstur = tekstur
        #super().__init__(rasa, tekstur, nama, bahan)

    def CitaRasa (self):
        return self.rasa
    
    def teksturNya (self):
        return self.tekstur

cemilan1 = Cemilan("Odading", "terigu")
rasa1 = Rasa("anjiimm banget", "gurih bangeed")
print ("Nama Cemilan : %s "% cemilan1.namaCemilan())
print ("Bahan Cemilan : %s "% cemilan1.bahanCemilan())
print("Rasanya : %s "% rasa1.CitaRasa())
print("Teksturnya :%s "% rasa1.teksturNya())
#rasa1.nama = "JEding"
print(rasa1.CitaRasa())
print(rasa1.nama)
"""

#konsep class
#class itu membungkus variable, function dll. dan merubahnya menjadi object
#class didalam classs juga bisa

"""
class Mamalia:
    def __init__(self, jenis):
        xxx xxx

class Cat(Mamalia):
    pass #akan mengambil property dari class Parent, tanpa harus punya mendefine propertynya terlebih daulu di class ini
"""

#Dictionaries
#fungsinya sama sama list. menyimpan baris data
phonebook = {}
phonebook["John"] = 93242343233
phonebook["Jack"] = 99324234234
phonebook["Jill"] = 99435656555
print(phonebook)

list = ["Galih", "Raka"]
dict = {"nama":"Galih", "Nama":"Raka", 4:"Empat"}
print(dict["nama"])

phone = {
    "John": +6234343432,
    "Jack": +6234344353,
    "Doe": +6234354432,
    "myList": [1,2,5,7]
}
#phone["myList"] = [4,5,7]
phone["Luke"] = +62778877

print(phone["John"])
print(phone["myList"])
print(phone["Luke"])

resistent = [
    {
        "name": "Luke",
        "role": "Jedi",
        "email": "luke@email.com"
    },
    {
        "name": "John",
        "role": "Pilot",
        "email": "john@email.com"
    }
]
for x in resistent:
    print(x)

phones = {"John Doe": 2423423423, "Max Speed": 4535345345}
for i, v in phones.items():
    print(i, v)

for i, v in phones.items(): #fungsi untuk nggeprint index langsung dengan valuenya
    print(f"Name: {i}, phone: {v}")

#delete John Doe
#del phones["John Doe"] #
phones.pop("John Doe") #pop ngeluarin data dari dict. tapi kita bisa nyimpen datayang dikeluarkan itu
#dict1 = phone.pop("John Doe") #contoh penggunaan. tapi yang tersimpan ke var dict cuman valuenya saja
""
"""
#Tupple
#Yupple mirip dengan list dan dictionary
tp = ("Kambing", "Kerbau", "Sapi") #kyak array. cuman tidak bisa diubah ubah
#datanya tidak bisa dihapus, tapi tupplenya bisa di hapus
#kalo mau diganti, biasanya ditransfer dulu ke list
print(tp)
ls = list(tp)
#ls[0] = "gukguk"
#print(ls)
#print(tp)
"""