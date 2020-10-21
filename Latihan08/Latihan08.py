#complexNumber

class ComplexNumber:
    glbl = "Hello" #direkomendasikan jangan buat var disini, gampang di hack

    #class constructor
    def __init__(self, r=0,i=0): #fungsi khusus constructor
        #biar kita bisa langusng dapat data awal tanpa harus input terlebih dahulu
        self.real = r
        self.imag = i

    def get_data(self):
        #print(f"{self.real} + {self.imag}") #untuk return string
        print(self.real + self.imag) #untuk return number

num1 = ComplexNumber(2,3)

num1.get_data()

print(num1.glbl)

#OOP 
# Polymorphism
# Inheretance
# Encapsulation
# Abstraction

# menurut penelitian, sesuatu yang diulang sebanyak 36 kali, pasti akan ingat.
