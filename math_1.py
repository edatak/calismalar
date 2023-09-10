# # Yntem 1
# # import math as islem
# # import math

# # value = dir(math)
# # value = math.fabs(8)
# # value = math.factorial(7)
# # value = math.atan(75)
# # print(value)

# #value = islem.copysign(77,5)

# #Yöntem 2
# # from math import *  # * sembolü kütüphanede her şeyi kapsıyor.
# # value = sqrt(9)
# # print(value)

# #random modülü
# import random
# result =dir(random)

# result = random.random() * 100
# result = int(random.uniform(10,50))
# result = int(random.randint(1,100))

# greeting = "Hello There"
# names = ["Sinan", "Cemre", "Eda","Özgün"]
# result = names[random.randint(0, len(names)-1)]
# result = random.choice(names)   # Herhangi seçtiği bir ögeyi yazdırır.
# result = random.choice(greeting)

# liste = list(range(10))
# random.shuffle(liste)    #Listeyi karışık verdi.
# result = liste

# liste = range(100)
# result = random.sample(liste,3)  #karışık olarak 3 sayı verdi.
# print(result)

# Kendi Modülü Oluşturma
'''
 Modül hakkında bilgilendirme
'''

print("Modül eklendi.")
number = 10

numbers = [1,2,3]

person = {
    "name" : "Ali" ,
    "age" : "29" ,
    "city" : "Ankara"
}
def func(x):
    '''
             fonsiyon hakkında bilgilendirme
    '''
    print(f"x: {x}")

class Person:
    def speak(self):
        print("I am speaking")



# Bu klasörü kapatıp farklı bir dosya açılıp importla kendi math_1 modülünü oluşturduk.
import math_1

# result = help(math_1)
# result = help(math_1.func)
result = math_1.number
result = math_1.numbers
result = math_1.person["name"]
result = math_1.person["age"]
result = math_1.func(10)

p = math_1.Person()
p.speak()


print(result)