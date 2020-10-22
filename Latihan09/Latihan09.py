#class itu fungsinya 
#inherit = penurunan sifat ke turunannya, sifat itu atribut didalam class
#membungkus atribut seperti variable, function. yang nantinya mereka akan bekerja sesuai kebutuhhannya
#class ada parrent ada child

class Car:
    def __init__(self, maxSpeed=0, mileage=0):
        self.maxSpeed = maxSpeed
        self.mileage = mileage

    def getMaxSpeed(self):
        return self.maxSpeed

    def getMileage(self):
        return self.mileage

#second class #class child
class Toyota(Car): #class toyota extend ke car
    def __init__(self, model=None, color=None):
        self.model = model
        self.color = color
    
    def getModel(self):
        return self.model

    def getColor(self):
        return self.color
    
    #jangan sering dipake, ini untuk spesial case aja
    @classmethod #method decorator
    def getOwner(cls):
        print("This is owner")
    #==========================================

toyo = Toyota("camry", "Black")
print(f"Model Toyo: {toyo.model}")

toyo.maxSpeed = 200
print(f"Max Speed Toyo: {toyo.getMaxSpeed()}")

Toyota.getOwner()

#extend, untuk menurunkan atibut ke kelas baru

#instance
carX = Car(380, 1000)

#call Property
print(f"Makx Speed: {carX.getMaxSpeed()}")
print(f"Mileage: {carX.getMileage()}")
