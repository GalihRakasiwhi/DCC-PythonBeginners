personAndPets = [
    {
        "name": "John Doe",
        "pets": [
            {"name": "Rooster"},
            {"name": "Dog"}
        ]
    },
    {
        "name": "Luke Skywalker",
        "pets": [
            {"name": "Duck"},
            {"name": "Camel"}
        ]
    },
    {
        "name": "Padme Amidala",
        "pets": [
            {"name": "Bird"},
            {"name": "Fish"}
        ]
    }
]

#bikin class personpet, person, pet
#menampilkan list data person dan pet
#menampilkan pet by person
#menampilkan person by pet
#menampilkan true or false, apakah jon punya pet anu, apakah pet anu milik john

class PersonPets:
    def __init__(self, person=None, pets=None):
        self.person = person
        self.pets = pets

    def getPetByPerson(self):
        for x in personAndPets:
            if x["name"] == self.person:
                print(x)

    def getPetAja(self):
        for x in personAndPets:
            if x["name"] == self.person:
                for p in x["pets"]:
                    print(p["name"])
                    #print(p)

    def getPersonByPet(self):
        for x in personAndPets:
            for p in x["pets"]:
                if p["name"] == self.pets:
                    print(x["name"])

    def getPersonByPetV2(self): #versi bang sukma
        for x in personAndPets:
            for p in x["pets"]:
                if p["name"] == self.pets:
                    print("Person: " + x["name"])
                    print(p["name"])
                    fstartApp()
        print("Liat yang bener! ULANGI LAGI")
        fstartApp()

    def cekMilik(self):
        for x in personAndPets:
            if (x["name"] == self.person):
                for p in x["pets"]:
                    if p["name"] == self.pets:
                        print("True")
                        fstartApp()
        print("False")

#getPersonByPetV2a = PersonPets(pets = "Dog")
#getPersonByPetV2a.getPersonByPetV2()

def fstartApp():
    print("\n==========")
    print("What to do? (Tulis Angka untuk Lanjut!)")
    print("1. Show all data on the list!")
    print("2. Show Pet by Person!")
    print("3. Show Person by Pet!")
    print("4. Show Person by Pet! Versi Bang Sukma")
    print("5. Cek Milik!\n")

    pilih = None
    pilih = input("")
    if(pilih == "1"):
        print("1. Show all data on the list!")
        #menampilkan list person dan pet
        print("\n#menampilkan list person dan pet")
        for x in personAndPets:
            print(x)
        fstartApp()

    elif(pilih == "2"):
        print("2. Show Pet by Person!\n\nList Name Person: ")
        for listName in personAndPets:
            print(">> " + listName["name"])
        print("\n")
        namePerson = input("Type the name person: ")
        for listName in personAndPets:
            if (namePerson == listName["name"]):
                print("Pets owned by %s is: " % namePerson)
                petAja = PersonPets(person = namePerson)
                petAja.getPetAja()
                fstartApp()
            
        print("Liat yang bener! ULANGI LAGI")
        fstartApp()
        """
        print("Pets owned by %s is: " % namePerson)
        petAja = PersonPets(person = namePerson)
        petAja.getPetAja()
        fstartApp()
        """

    elif(pilih == "3"):
        print("3. Show Person by Pet!\n\nList Name Pets: ")
        for x in personAndPets:
            for namePets in x["pets"]:
                print(">> " + namePets["name"])
                #print(namePets)
                #print(namePets.values())
        print("\n")
        namePet = input("Type the name pet: ")
        for x in personAndPets:
            for namePets in x["pets"]:
                if (namePets["name"] == namePet): #biasakan data dari list disebelah kiri,
                    print("Person who owned %s is: " % namePet)
                    getPerson = PersonPets(pets = namePet)
                    getPerson.getPersonByPet()
                    fstartApp()
                
        print("Liat yang bener! ULANGI LAGI")
        fstartApp()
        """
        print("Person who owned %s is: " % namePet)
        getPerson = PersonPets(pets = namePet)
        getPerson.getPersonByPet()
        fstartApp()
        """

    elif(pilih == "4"):
        print("4. Show Person by Pet! Versi Bang Sukma\n\nList Name Pets: ")
        for x in personAndPets:
            for namePets in x["pets"]:
                print(">> " + namePets["name"])
        print("\n")
        namePet = input("Type the name pet: ")
        getPersonByPetV2a = PersonPets(pets = namePet)
        getPersonByPetV2a.getPersonByPetV2()        

    elif(pilih == "5"):
        print("4. Ownership Check!")
        namePerson = input("Type name person: ")
        namePets = input("Type name pet: ")
        cekMilik1 = PersonPets(person = namePerson, pets = namePets)
        cekMilik1.cekMilik()

    else:
        print("Baca yang bener!")

fstartApp()


"""
#menampilkan list person dan pet
print("\n#menampilkan list person dan pet")
for x in personAndPets:
    print(x)

#menampilkan pet by person
print("\n#menampilkan pet by person")
getPet = PersonPets(person = "Padme Amidala")
getPet.getPetByPerson()

#menampilkan pet aja
print("\n#menampilkan pet aja")
petAja = PersonPets(person = "Padme Amidala")
petAja.getPetAja()

#menampilkan person by pet
print("\n#menampilkan person by pet")
getPerson = PersonPets(pets = "Fish")
getPerson.getPersonByPet()

#menampilkan person by pet versi Bang Sukma
getPersonByPetV2a = PersonPets(pets = "Dog")
getPersonByPetV2a.getPersonByPetV2()

#Ownership Check
cekMilik1 = PersonPets(person = "John Doe", pets = "Dog")
cekMilik1.cekMilik()
"""


"""
for x in personAndPets:
    for n in x["name"]:
       print(n)

#menampilkan semua pet didalam list
print("\n#menampilkan semua pet didalam list")
for x in personAndPets:
    for p in x["pets"]:
       print(p)

#Menampilkan pets by name
print("\n#Menampilkan pets by name")
for x in personAndPets:
    if x["name"] == "Padme Amidala":
        for p in x["pets"]:
           print(p)
"""