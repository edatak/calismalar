####### FOR DÖNGÜLERİ ######

# sayilar = [1,3,5,7,9,12,19,21]
# for sayi in sayilar:
#     if (sayi%3==0) :          (3'ün katıu olan sayılar)
#         print(sayi)

# toplam = 0
# for sayi in sayilar:           (verilen sayıların toplamı)
#     toplam += sayi
# print("toplam:" , toplam)


# for sayi in sayilar:
#  if (sayi % 2 ==1):          (tek sayıların karesi.)
#   print( sayi **2)

# sehirler = ["Kocaeli" , "İstanbul" , "Ankara" , "İzmir" , "Rize"]

# for i in sehirler:
#     if (len(i) <= 5 ):    (en fazla 5 harfliler yazılacak.)
#      print(i)

# urunler = [
#     {"name" : "samsung S6" , "price" : "3000"},
#     {"name" : "samsung S7" , "price" : "4000"},
#     {"name" : "samsung S8" , "price" : "5000"},
#     {"name" : "samsung S9" , "price" : "6000"},
#     {"name" : "samsung S10" , "price" : "7000"},
# ]

# toplam = 0
# for urun in urunler:
#     fiyat = int(urun["price"])       (ürünlerin toplamı)
#     toplam += fiyat
# print("toplam ürün fiyatı:" , toplam)

# for urun in urunler:
#     if (int(urun["price"]) <= 5000):   (5000'den düşük veya eşit ürünler)
#         print(urun["name"])



##########  WHİLE DÖNGÜLERİ #########

# sayilar = [1,3,5,7,9,12,19,21]
# i = 0
# while (i < len(sayilar)):         (sayilari while döngüsüyle ekrana yazdırdık.)
#    print(sayilar[i]) 
#    i += 1


# baslangic = int(input("başlangıç: "))
# bitis = int(input("bitis: "))

# i = baslangic
# while i < bitis:             (Kullanıcıdan alınan başlangıç ve bitiş sayıları arasındaki tek sayılar.)
#     i += 1
#     if (i %2 == 1):
#      print(i)



# x = 100
# while x > 0 :
#    print(x)         (100'den geriye sayılar yazdııldı.)
#    x -= 1

# numbers = []

# i = 0
# while i < 5:
#     sayi = int(input("sayı:"))
#     numbers.append(sayi)        (Kullanıcıdan alınan 5 sayı küçükten büyüğe sıralandı.)
#     i += 1
# numbers.sort()
# print(numbers)



# Kullanıcıdan alınan adet sayısına göre isim ve fiyat alınıp listelendi.
# urunler = []
# adet = int(input("Kaç ürün eklemek istiyorsunuz: "))
# i = 0
# while (i<adet):
#     name = input("ürün ismi:")
#     price = input("ürün fiyatı: ")
#     urunler.append({
#         "name": name,
#         "price": price
#     })
#     i += 1
# for urun in urunler:
#     print( f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')

# break ve continue terimlerinde, break tanımlanan işleme kadar devam et durdur demekken, continue verilen işlemi geçip işleme devam et demek.

# range == int sıralama,  enumerate == str sıralama, zip == liste birleştirme

################## UYGULAMALAR ############

#OYUN#

import random
sayi = random.randint(1,100)
can = int(input("Kaç hak kullanmak istersiniz: "))
hak = can
sayac = 0

while hak > 0:
     hak -= 1
     sayac += 1
     tahmin = int(input("tahmin: "))

     if sayi == tahmin:
         print(f"Tebrikler {sayac}.defada bildiniz. Toplam puanınız: {100-(100/can) * (sayac-1)}")
         break
     elif sayi > tahmin:
         print("Yukarı")
     else:
         print("Aşağı")
     if hak == 0:
         print(f"Hakkınız bitti. Tutulan sayı: {sayi}")

# Girilen sayı asal mı değil mi?
sayi = int(input("sayı: "))
asalmi = True
if sayi ==1:
    asalmi = False
for i in range(2,sayi):
    if (sayi % i == 0) :
        asalmi = False
        break
if asalmi:
    print("Sayı asaldır.")
else:
    print("Sayı asal değildir.")