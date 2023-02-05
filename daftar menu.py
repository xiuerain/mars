makanan= ["nasi pecel","nasi goreng","nasi putih"]
minuman= ["air mineral","air susu","air es"]
print ("\tDaftar Menu\n")
print ("Makanan\t\tMinuman")
print ("1)Nasi Pecel\t4)Air mineral")
print ("2)Nasi Goreng\t5)Air Susu")
print ("3)Nasi Putih\t6)Air Es")
data_makan=input("Masukan pilihan makanan anda: ")
data_minum=input("Masukan pilihan minuman anda: ")
data_kasir=input("Masukan nama kasir: ")
data_pembeli=input("Masukan nama pembeli: ")
if data_makan=="1":
    data_makan=makanan[0]
if data_makan=="2":
    data_makan=makanan[1]
if data_makan=="3":
    data_makan=makanan[2]
if data_minum=="4":
    data_minum=minuman[0]
if data_minum=="5":
    data_minum=minuman[1]
if data_minum=="6":
    data_minum=minuman[2]
print("\n\n\t\tNota\n")
print("Kasir:",data_kasir)
print("Pembeli:",data_pembeli)
print("Nama Pesanan: ")
print("1) ",data_makan)
print("2) ",data_minum)
print("\t\t\tMalang\n\t\t\t2022")
