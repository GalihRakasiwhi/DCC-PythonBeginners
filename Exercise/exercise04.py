#fucntion menampilkan urutan bilangan yang habis dibagi 3, argumentnnya range

#def bilanganHabis3(parameter):
#    for bilangan in range(parameter):
#        if bilangan % 3 == 0:
#            if bilangan == 0:
#                continue
#            print (bilangan)
#        bilangan += 1
#
#bilanganHabis3(20)

#fucntion menampilkan urutan bilangan yang habis dibagi 3, argumentnnya range

def bilanganHabis3(parameter):
    if parameter == "" or parameter < 3:
        return
        
    for bilangan in range(parameter):
        if bilangan % 3 == 0:
            print (bilangan)

bilanganHabis3(20)

