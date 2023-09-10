# key - value

# sehirler = ["Kocaeli", "İstanbul"]
# plakalar = [41,34]

# print(plakalar[sehirler.index("İstanbul")])

# plakalar = {"Kocaeli": 41, "İstanbul": 34}
# print(plakalar["Kocaeli"])
# print(plakalar["İstanbul"])

# plakalar["Ankara"] = 6
# print(plakalar)

# users = {"EdaAtak": {
#     "yaş": 30, 
#     "meslek": ["öğretmen"], 
#     "email": "edatak@gmail.com", 
#     "adres": "Ankara", 
#     "telefon": "464513"}, 
# "SinanAtak":{
#     "yaş": 33, 
#     "meslek": ["Tekniker"], 
#     "email": "snnatak@gmail.com", 
#     "adres": "Ankara", 
#     "telefon":"454689"}}

# print(users["EdaAtak"])
# print(users["SinanAtak"]["yaş"])
# print(users["EdaAtak"]["adres"])

ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı:")
surname = input("öğrenci soyad:")
phone = input("öğrenci telefon:")

# ogrenciler[number] = {
#     "ad" : name,
#     "soyad" : surname,
#     "telefon" : phone
# }

ogrenciler.update({
    number: {
        "ad": name,
        "soyad" : surname,
        "telefon" : phone
    }
})


number = input("öğrenci no: ")
name = input("öğrenci adı:")
surname = input("öğrenci soyad:")
phone = input("öğrenci telefon:")

ogrenciler.update({
    number: {
        "ad": name,
        "soyad" : surname,
        "telefon" : phone
    }
})



number = input("öğrenci no: ")
name = input("öğrenci adı:")
surname = input("öğrenci soyad:")
phone = input("öğrenci telefon:")

ogrenciler.update({
    number: {
        "ad": name,
        "soyad" : surname,
        "telefon" : phone
    }
})
print(ogrenciler)


ogrNo = input("öğrenci no: ")
ogrenci = ogrenciler[ogrNo]
print(ogrenci)

print(f"aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")