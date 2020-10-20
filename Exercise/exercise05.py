#Func yang menampilkan tulisan saya programmer Python
#def tulisan(teks = None, baris = None):
#    for bil in range(baris):
#        print(teks)

#tulisan("Saya programmer Python", 10)

#def bilangan(x, y):
#    return x + y

#hasil = bilangan(10, 5)
#print(hasil)

#
def orang(nama, umur, hobi):
    print("Nama Saya %s" % nama + " Umur Saya %d" % umur + " Hobi saya %s" % hobi)
    print("Nama Saya %s, umur Saya %d, hobi saya %s" % (nama, umur, hobi))

orang("Galih", 15, "Makan")

def bilanganGanjil(bil):
    for x in range(bil):
        if x % 2 == 1:
            print(x)

bilanganGanjil(10)

def bilanganGenap(bil):
    for x in range(bil):
        if x == 0:
            continue
        if x % 2 == 0:
            print(x)

bilanganGenap(10)
