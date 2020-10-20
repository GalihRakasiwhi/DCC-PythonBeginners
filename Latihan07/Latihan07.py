def bilangan3(baris = None): #nilai default untuk baris, biar kalo argumennya kosong, tidak eror
        if baris ==None or baris < 3:
            return

        for bil in range(baris):
            if bil == 0:
                continue

            if bil % 3 == 0:
                print(bil)

bilangan3()

#def bilangan3(baris = None):
# Ketika kita memanggil tanpa mengisi argumen, dia tidak error 

def bilangan3while(baris = None): #nilai default untuk baris, biar kalo argumennya kosong, tidak eror
        if baris ==None or baris < 3:
            return

        index = 0
        while index < baris:
            if index != 0:
                if index % 3 == 0:
                    print(index)
            index += 1

bilangan3while(20)

#class and Object

class siswa:
    nama = "Galih Rakasiwhi"
    umur = 15

    def alamat(self):
        #print("Jl Banda No.40")
        return "Jl Banda No.40"
    def alamat2(self, almt):
        #print(almt)
        return almt

#Instansiasi, perubahan kelas menjadi Objek
objectSiswa = siswa()
print(objectSiswa.nama)
print(objectSiswa.umur)
print(objectSiswa.alamat())
print(objectSiswa.alamat2("Komplek beruang"))
#overide property didalam class siswa
objectSiswa.nama = "Jacob"
print(objectSiswa.nama)