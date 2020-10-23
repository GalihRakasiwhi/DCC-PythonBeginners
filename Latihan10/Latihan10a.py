tp = ("Kambing", "Kerbau", "Sapi") 
print(tp)
ls = list(tp)
ls[0] = "Kucing"
print(ls)
print(tp)


x1 = [1,2,3]
x2 = [1,2,3]
if x1 is x2:
    print("OK")
else:
    print("Salah")

#is tidak mengecek jenis. tapi memang mengecek. apakah yang ditunjuk itu adalah memang yang sedang ditunjuk 