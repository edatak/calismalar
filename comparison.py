#KARŞILAŞTIRMA OPERATÖRLERİ
# username, password => database

# "edaatak", "123456"

# a, b, c, d = 5, 5, 10, 4
# password = "1234"
# username = "edaatak"

# result = a == b #True
# result = a == c #False
# result = ("edaatak" == username) #True
# result = (a !=b)  #False geldi, eşit değil denildiğii için.
# result = (a < c) #True
# result = (a >= b) #True
# result = (True ==1)
# result = (False+ True+ 40)
# print(result)

# a = int(input("a: "))
# b = int(input("b: "))

# result = (a>b)
# print(f"a: {a} b: {b} den büyüktür: {result}")

# vize1 = float(input("1.vize: "))
# vize2 = float(input("2.vize: "))
# final = float(input("final:"))

# ortalama = (((vize1+vize2) /2) * 0.6) + (final * 0.4)

# print(f"Nor ortalamanız : {ortalama} ve dersten geçme durumunuz: {ortalama>=50}")

# sayi = int(input("sayı:"))

# tekcift = (sayi % 2 == 0)
# print(f"Girilen sayı çift olma durumu: {tekcift}")

# sayi = int(input("sayı: "))
# pozitifmi = (sayi>0)
# print(f"Girilen sayının pozitif olma durumu: {pozitifmi}")

# email = "email@edatak.com"
# password = "abc123"

# girilenEmail = input("email:")
# girilenPassword = input("parola:")

# isEmail = (email == girilenEmail) buraya girilenEmail.lower().strip() dediğimizde lower büyük küçük harfi düzelt demek, strip boşluğu önemseme demek.
# isPassword = (password == girilenPassword)

# print(f"Email bilgisi doğrumu: {isEmail} ve Parola doğru mu: {isPassword}")

###### KARŞILAŞTIRMA OPERATÖRLERİ ######

# x = 5
# hak = 5
# devam = "e"
# result = 5 <x <10

# #and
# result = x>5 and x<10 
# result = (hak>0) and (devam =="e")

# #or
# result = (x>0) or (x % 2 ==0)

# #not

# result = not( x > 0)

# #z, 5-10 arasında olan bir çift sayı mı?

# result = ((x>5) or (x<10)) and (x%2==0)

# print(result)

#Sayı 0-100 arasında mıdır?
# sayi = float(input("sayı:"))
# result = ((sayi > 0) and (sayi < 100))
# print(f"1Sayı 0-100 arasında mı : {result}")

# Sayı pozitif çift olup olmadığını kontrol et.
# sayi = int(input("sayı:"))
# result = ((sayi > 0) and (sayi %2 == 0))
# print(f"Sayı pozitif çift mi: {result}")

# Email ve parola giriş kontrolü.
# email = "edatak@gmail.com"
# parola = "789klm"

# girilenEmail = input("email:")
# girilenParola = input("parola:")

# result = (girilenEmail == email) and (girilenParola == parola)
# print(f"Uygulamaya giriş başarılı mı:{result}")

#Girilen üç sayıyı büyüklük olarak karşılaştır.

# a = int(input("a:"))
# b = int(input("b:"))
# c = int(input("c:"))

# result = (a>b) and (a>c)
# print(f"a en büyük sayıdır : {result}")

# result = (b>a) and (b>c)
# print(f"b en büyük sayıdır: {result}")

# result = (c>a) and (c>b)
# print(f"c en büyük sayıdır: {result}")

# vize1 = float(input("1.vize:"))
# vize2 = float(input("2.vize:"))
# final = float(input("final:"))

# ortalama = ((vize1+vize2) / 2) *0.6 and (final * 0.4)
# #result = (ortalama >=50) and (final >=50)
# result = (ortalama >=50) or (final >=70)
# print(f"Öğrencinin oratalaması: {ortalama} ve geçme durumu : {result}")

#Kişin ad,kilo, boy bilgisi sorgulama ve index hesaplama.
# name = input("name:")
# kilo = float(input("kilo:"))
# boy = float(input("boy:"))
# index = (kilo) / (boy ** 2)
# zayif = (index >= 0) and (index <=18.4)
# normal = (index >18.4) and (index <= 24.9)
# fazlakilolu = (index >=25) and (index<=29.9)
# obez = (index>=30.0) and (index<=34.9)


# print(f"{name} kilo indeksin : {index} ve kilo değerlendirmen zayıf: {zayif}")
# print(f"{name} kilo indeksin : {index} ve kilo değerlendirmen normal: {normal}")
# print(f"{name} kilo indeksin : {index} ve kilo değerlendirmen fazla kilolu: {fazlakilolu}")
# print(f"{name} kilo indeksin : {index} ve kilo değerlendirmen obez: {obez}")

