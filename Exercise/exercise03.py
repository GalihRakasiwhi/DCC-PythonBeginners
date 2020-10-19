#Buat baris bilangan genap 1 - 10

for genap in range (1, 11):
    if genap % 2 == 1:
        continue
    print(genap)
    genap += 1

#buat baris bilangan ganjil 1 10
for ganjil in range (1, 11):
    if ganjil % 2 == 0:
        continue
    print(ganjil)
    ganjil += 1

ls = [1,5,6,10,2,3]
index = 0
while index < len(ls):
    print(ls[index])
    index += 1
