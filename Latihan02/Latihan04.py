astring = "Hello World, aduh, yaya yayay, aaa duh"
alist = astring.split(" ")

print(astring.index("o")) #cek index keberapa huruf o berada, yang diitung huruf o pertama
print(astring.count("l")) #ada berapa huruf l di var astring 
print(astring[3:8:2]) #start:stop:step
print(astring.upper()) #ubah astring jadi kapital semua
print(astring.lower()) #ubah astring jadi huruf kecil semua
print(astring.startswith("Hello")) #cek apakah value astring dimulai dari kata "Hello"
print("Split Sample:%s" % astring.split(",")) #split/pisahkan string yang ada di var astring dengan carackter ","

#condition
x = 2
if x == 2:
    print(x) 

if "Hello" in alist:
    print("Yes, i have")

print(len(alist))

#elif = else if

x = [1,2,3]
y = [1,2,3]
print (x == y) #cek apakah value x sama dengan value y?
print (x is y) #cek apakah instance x adalah instansi y?

#Not Operator
#true true = true
#true false = false
#false true = false
#false false = false

