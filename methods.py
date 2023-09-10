# def change(n):
#     n[0] = "Beril"

# isimler = ["Selin", "Melis" , "Yağmur"]
# change(isimler)
# print(isimler)

# def add(*params):
#     print(params)
#     return sum((params))
# print(add(25,34,69,22))

# def displayUser(**args):
#     print(type(args))
#     for key, value in args.items():
#       print("{} is {}". format(key,value))

# displayUser(name= "Eda" , age= 29, city="Ankara")
# displayUser(name= "Sinan" , age= 32, city="Ankara", phone="456987")
# displayUser(name= "Cemre" , age= 1.5, city="Ankara", phone="452123", email= "cmratak@hotmail.com")


# def yazdir(kelime, adet):
#     print(kelime * adet)
# yazdir("Merhaba\n" , 10)

# def listeyeCevir(*args):
#     liste = []

#     for arg in args:
#         liste.append(arg)

#     return liste
# result = listeyeCevir(10,20,30, "Merhaba",)
# print(result)



# def asalSayilariBul(sayi1 , sayi2):
#     for sayi in range(sayi1 , sayi2+1):
#        if sayi >1:
#            for i in range(2,sayi):
#               if (sayi % i == 0):
#                   break
#            else:
#             print(sayi)

# sayi1 = int(input("Sayı 1:"))
# sayi2 = int(input("Sayı 2:"))

# asalSayilariBul(sayi1, sayi2)

# def tamBölenleriBul(sayi):
#     tamBolenler = []

#     for i in range(2,sayi) :
#        if sayi % i == 0 :
#            tamBolenler.append(i)
#     return tamBolenler
# print(tamBölenleriBul(20))

#########Bankamatik uygulamaları######
EdaHesap = {
    "ad" : "Eda Atak",
    "hesapNo": "123654",
    "bakiye" : 5000,
    "ekHesap" : 7000
}
CemreHesap = {
    "ad" : "Cemre Atak",
    "hesapNo": "123645654",
    "bakiye" : 10000,
    "ekHesap" : 3000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye'] >= miktar :
        hesap['bakiye'] -= miktar
        print("Paranızı alabilrsiniz.")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek hesap kullanılsın mı(e/h)")

            if ekHesapKullanimi =="e":
                bakiye = hesap['bakiye']

                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz.")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")

        else:
            print("Üzgünüz bakiye yetersiz.")
            bakiyeSorgula(CemreHesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")



paraCek(CemreHesap, 15000)

print("****************")

paraCek(CemreHesap, 2000)



