list = [1,2,3]
tuple = (1,"iki",3)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(tuple))

list = ["Ali", "Veli"]
tuple = ("Damla", "Ayşe", "Ayşe")

# list[0] = "Ahmet"
# tuple[0] = Deniz #Tuple'da eleman değiştiremezsin. Bu yüzden bu kod geçersiz.
print(tuple.count("Ayşe"))
names = ("Emel", "Arda", "Sezen") + tuple
print(names)
