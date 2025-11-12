# # append()	ro'yhat oxiriga element qo'shish
# cars = ['lasetti', 'malibu', 'byd', 'bmw']
# cars.append('nexia 3')
# print(cars)
#
# cars.append('labo')
# print(cars)
#
#
#
# # clear() - ro'yhatni tozalash
# cars = ['lasetti', 'malibu', 'byd', 'bmw']
# cars.clear()
# print(cars)
#
# m = ['lasetti', 'malibu', 'byd', 'bmw', 'nexia 3', 'labo']
# m.clear()
# print(m)
#
#
#
# # copy() - ro'yhatdan nusha olish
# meva = ['olma', "o'rik", 'shaftoli']
# a = meva.copy()
# print(a)
#
# sonlar = [12,34,56,78]
# b = sonlar.copy()
# print(b)
#
#
#
# # count()
# son = [12, 13, 34, 45, 65]
# c = son.count(12)
# print(c)
#
# son = [12, 13, 34, 45, 65, 13, 75, 75, 13]
# c = son.count(13)
# print(c)



# extend() - ikki ro'yhatni qo'shish
# meva = ['olma', 'shaftoli', 'gilos']
# cars = ['audi', 'BMW', 'Volvo']
# meva.extend(cars)
# print(meva)
#
# ovqatlar = ['shashlik', "so'msa", 'shaverma', 'lavash']
# son = [1, 2, 3, 4,]
# son.extend(ovqatlar)
# print(son)



# index() - ro'yhat elementini indeksini aniqlash
# meva = ['olma', 'shaftoli', 'gilos', 'banan', 'olcha']
# a = meva.index('banan')
# print(a)
#
# cars = ['audi', 'BMW', 'Volvo']
# b = cars.index('BMW')
# print(b)



# insert() - indeks orqali element qo'shish
# meva = ['olma', "o'rik", 'shaftoli']
# meva.insert(0, 'behi')
# print(meva)
#
# meva.insert(2, 'gilos')
# print(meva)



# pop() - indeks orqali element o'chirish
# meva = ['behi', 'olma', 'gilos', "o'rik", 'shaftoli']
# meva.pop(1)
# print(meva)
#
# meva.pop(3)
# print(meva)



# remove() = element nomi bilan o'chirish
# meva = ['behi', 'olma', 'gilos', "o'rik", 'shaftoli']
# meva.remove('olma')
# print(meva)
#
# meva.remove("o'rik")
# print(meva)



# reverse()	- ro'yhatni teskari tartibda joylashtiradi
# cars = ['audi', 'BMW', 'Volvo', 'lasetti']
# cars.reverse()
# print(cars)
#
# meva = ['behi', 'olma', 'gilos', "o'rik", 'shaftoli']
# meva.reverse()
# print(meva)



# sort() - ro'yhatni a dan z-gacha tartiblaydi
cars = ['audi', 'bmw', 'volvo', 'lasetti']
cars.sort()
print(cars)

meva = ['behi', 'olma', 'gilos', "o'rik", 'shaftoli']
meva.sort()
print(meva)
