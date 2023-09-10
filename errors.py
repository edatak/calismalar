liste = ["1" ,"2", "5a", "10b","abc", "10", "50"]

# for x in liste:
#     try:
#         result= int(x)
#         print(result)     Listedeki sayıları çıktı aldık.
#     except ValueError:
#         continue



# while True:
#     sayi = input("sayı: ")
#     if sayi == "q":
#        break

#     try:                      Girilen sayıları ekrana float değerle yazdırdı, harf yazıldığında hata verdi.
#         result = float(sayi)
#         print("Girdiğiniz sayı: ", result)
#         break
#     except ValueError:
#         print("Geçersiz sayı")
#         continue





# def checkPassword(parola):
#     turkce_karakterler = "şçğüöıİ"

    
#     for i in parola:
#         if i in turkce_karakterler:
#            raise TypeError("Parola Türkçe karakter içeremez.")
#         else:
#             pass
#     print("Geçerli parola")

# parola = input("Parola: ")

# try:                          (Girilen parolanın Türkçe karakter içermemesi için yazılan kod)
#     checkPassword(parola)
# except TypeError as err:
#     print(err)




#Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajı vereceğiz.


# def faktoriyel(x):
#     x = int(x)

#     if x < 0:
#         raise ValueError("Negatif değer")
    
#     result= 1

#     for i in range(1, x+1):
#         result *= i

#     return result

# for x in [5,10,20, -3, "10a"]:
#     try:
#         y= faktoriyel(x)
#     except ValueError as err:
#         print(err)
#         continue
#     print(y)


