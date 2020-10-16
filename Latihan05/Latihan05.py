#loop for
prime = [2,3,5,7]
for prime in prime:
    print(prime)

#print out 0,1,2,3,4
for x in range(5):
    print(x)

#print out 3,4,5
for x in range (3, 6):
    print(x)

#print out 3,4,7


#while
count = 0
while count <5:
    print(count)
    count += 1

#break
#pirnt out  0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if (count >= 5): #saat var count lebih dari sama dengan 5, langsung break, keluar dari perintah
        break

#continue
#print out only 1,3,5,7,9
for x in range(10): #range dari 0-10
    if x % 2 == 0: #jika x modulu 2 == 0
        continue # lanjut aja bro, gak usah ikuti perintah dibawah lu (diblok yang sama ya)
    print(x)

