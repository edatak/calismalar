# file = open("Newfile.txt", "r")
# file.close()

# file = open("C:/users/edaatak/desktop/newfile.txt", "w")
# print(file)

# encoding = "utf-8" türkçe karakterleri de yazması için ekledik.

# file = open("Newfile.txt", "w", encoding="utf-8")
# file.write("Eda Atak")
# file.close()


# a ile dosyaya bilgi ekleme işlemi.
# file = open("Newfile.txt", "a", encoding="utf-8")
# file.write("\nSinan Atak")
# file.close()

# x oluşturma. Dosya varsa hata oluşur.
#file = open("Newfile.txt", "x", encoding="utf-8")

# r dosya okuma
# try:
#     file = open("newfile2.txt", "r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma hatası")
# finally:
#     print("Dosya kapandı")
#     file.close()


# file = open("Newfile.txt", "r", encoding="utf-8")
# for i in file:
#     print(i, end= "")
# file.close()

# content1 =file.read()
# print("İçerik 1")
# print(content1)
# content2 =file.read()
# print("İçerik 2")
# print(content2)
# file.close()

# content = file.read(5)
# content = file.read(3)
# print(content)
# file.close()



################readline() fonksiyonu #################
# print(file.readline(), end = "")
# print(file.readline(), end = "")
# print(file.readline(), end = "")
# file.close()


################readlines() fonksiyonu #################

# liste = file.readlines()
# print(liste[1])

# file.close()


# with open("newfile.txt" , "r+", encoding = "utf-8") as file:
#     list=file.readlines()
#     list.insert(3, "Begüm Atak\n")
#     file.seek(0)
#     file.writelines(list)

# with open("newfile.txt" , "r" , encoding= "utf-8") as file:
#     print(file.read())




##################### UYGULAMA ##############
def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    ogrenciAdi = (liste[0])
    notlar = (liste[1]).split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1+not2+not3) / 3

    if ortalama >= 90 and ortalama<=100:
        harf ="AA"
    elif ortalama >=85 and ortalama <=89:
        harf = "BA"
    elif ortalama >=80 and ortalama <=84:
        harf= "BB"
    elif ortalama >=75 and ortalama <=79:
        harf= "CB"
    elif ortalama >=70 and ortalama <=74:
        harf = "CC"
    elif ortalama >= 65 and ortalama <=64:
        harf = "DD"
    elif ortalama >=50 and ortalama <=59:
        harf= "FD"
    else:
        harf = "FF"
    
    return ogrenciAdi + ": " + harf + "\n"

def ortalamalari_oku():
     with open("sinav_notlari.txt", "r", encoding= "utf-8") as file:
       for satir in file:
           print(not_hesapla(satir))
def not_gir():
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyad: ")
    not1 = input("not 1: ")
    not2 = input("not 2: ")
    not3 = input("not 3: ")

    with open("sinav_notlari.txt" , "a" , encoding = "utf-8") as file:
        file.write(ad + " " + soyad+ ":" +not1+"," +not2+","+not3+"\n")
def notlari_kayitet():
    with open("sinav_notlari.txt", "r", encoding= "utf-8") as file:
        liste=[]

        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt", "w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

while True:
    islem = input("1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış")

    if islem == "1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notlari_kayitet()
    else:
        break