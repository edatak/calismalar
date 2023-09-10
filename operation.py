# Identity operator : is

# x = y = [1 , 2 , 3]
# z =  [1, 2, 3]

# print(x==y)
# print(x==z)
# print(x is y)
# print(x is z)

# x = [1 , 2 , 3]
# y = [2, 4]

# del x[2]
# y[1] = 1
# y.reverse()
# print(x==y)
# print(x is not y)

# # Membership operatör: in

# x = ["apple", "banana"]
# print("banana" in x)

# name = "Cemre"
# print("e" not in name)


#############IF VE ELSE BLOKLARI############

# username ="edatak"
# password = "1234"

# if (username == "edatak" ):
#     if (password == "12345") :
#        print("Hoş geldiniz")
#     else :
#        print("parola yanlış")
# else:
#     print("username yanlış")

# x = int(input("x: "))
# y = int(input("y: "))

# if x > y :
#     print("x y den büyük")
# elif x == y:
#     print("x y eşit")
# else:
#     print("y x den büyük")

# num = int(input("sayı:"))

# if num > 0:
#     print("sayı pozitif")
# elif num < 0 :
#     print("sayı negatif")
# else:
#     print("sayı 0 a eşit")

# demo
# name = input("isim: ")
# age = int(input("yaş: "))
# education = input("eğitim: ")

# if (age>=18):
#     if (education == "lise" or education == "üniversite"):
#        print(f"{name} ehliyet alabilirsin.")
#     else:
#        print(f"{name} ehliyet alamazsın, eğitim durumun yetersiz.")
# else:
#     print(f"{name} ehliyet alamazsın, yaşın tutmuyor.")

# yazili1 = int(input("1.sınav: "))
# yazili2 = int(input("2.sınav: "))
# sözlü = int(input("Szölü: "))
# ortalama = (yazili1 + yazili2 + sözlü ) / 3

# if (ortalama >= 0) and (ortalama <25):
#     print(f" ortalamanız: {ortalama} notunuz : 0")
# elif (ortalama >=25) and (ortalama <45):
#     print(f" ortalamanız: {ortalama} notunuz : 1")
# elif (ortalama >=45) and (ortalama <55):
#     print(f" ortalamanız: {ortalama} notunuz : 2")
# elif (ortalama >=55) and (ortalama <70):
#     print(f" ortalamanız: {ortalama} notunuz : 3")
# elif (ortalama >=70) and (ortalama <85):
#     print(f" ortalamanız: {ortalama} notunuz : 4")
# elif (ortalama >=85) and (ortalama <=100):
#     print(f" ortalamanız: {ortalama} notunuz : 5")
# else:
#     print("Yanlış bilgi girdiniz.")

# import datetime

# tarih = input("Aracınız hangi tarihte trafiğe çıktı (2023/7/11): ")
# tarih = tarih.split("/")
# trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
# simdi = datetime.datetime.now()
# fark = simdi - trafigeCikis
# days = fark.days

# if days <=365:
#     print("1.servis aralığı")
# elif days > 365 and days <= 365*2:
#     print("2.servis aralığı")
# elif days > 365*2 and days<=365*3:
#     print("2.servis aralığı")
# else:
#     print("Hatalı süre.")

##### DEMO ####
# sayi = float(input("sayı: "))
# if (sayi > 0) and (sayi <= 100) :
#     print("Sayı 0 ile 100 arasında.")
# else:
#     print("Sayı 0 ile 100 arasında değildir.")




# sayi = int(input("Sayı: "))
# if (sayi > 0): 
#     if (sayi % 2 == 00 ):
#      print("girilen sayı pozitif çift sayıdır.")
#     else:
#        print("Girilen sayı pozitif ancak tek sayıdır.")
# else:
#     print("Girilen sayı negatif sayıdır.")



# email = "edatak@gmail.com"
# password = "abc123"

# girilenEmail = input("email: ")
# girilenPassword = input("Password: ")

# if (girilenEmail == email):
#     if(girilenPassword == password):
#         print("Uygulamaya giriş başarılı")
#     else:
#         print("Password yanlış")
# else:
#     print("Email hatalı.")

# a = int(input("a:"))
# b = int(input("b:"))
# c = int(input("c:"))

# if (a>b) and (a>c):
#    print(f"a en büyük sayıdır.")

# elif (b>a) and (b>c):
#    print(f"b en büyük sayıdır.")

# elif (c>a) and (c>b):
#    print(f"c en büyük sayıdır.")



# vize1 = float(input("1.vize:"))
# vize2 = float(input("2.vize:"))
# final = float(input("final:"))

# ortalama = ((vize1+vize2) / 2) *0.6 + (final * 0.4)
# if (ortalama >=50):
#     if (final >=50):
#       print(f"Öğrencinin ortalaması: {ortalama} ve geçme durumu : başarılı")
#     else:
#       print(f"Öğrencinin ortalaması: {ortalama} ve geçme durumu : başarısız. Finalden en az 50 almalısınız.")

# else:
#  print(f"Öğrencinin ortalaması: {ortalama} ve geçme durumu : başarısız")

# if (ortalama >=50):
#     print(f"Öğrencinin ortalaması: {ortalama} ve geçme durumu : başarılı")
# else:
#     if (final >=70):
#         print(f"Öğrencinin ortalaması: {ortalama} ve geçme durumu başarılı. Finalden en az 70 aldığınız için geçtiniz.")
#     else:
#         print(f"Öğrencinin ortalaması: {ortalama} ve geçme durumu başarısız.")


