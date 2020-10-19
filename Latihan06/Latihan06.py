#functon
def fNama(nama):
    print("Hello %s" % nama)
    print(f"Hello, {nama}")

def secondFunc():
    nama = "Luke Skywalker"
    return fNama(nama)

#print bilagan negative
def printNegative(index, length):
    if index == "" and length == "":
        return


    while index < length:
        if index % 2 == 1:
            print(index)
        index += 1

fNama("Galih")

secondFunc()

printNegative(0, 10)