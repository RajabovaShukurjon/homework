# capitalize()- birinchi harfni katta harfga o'zgartiradi
# ism = "shukurjon"
# familiya = "Rajabova"
# ism_familiya = (f"{ism} {familiya}")
# print(ism_familiya.capitalize())
#
# ism = "SHUKURJON"
# familiya = "RAJABOVA"
# ism_familiya = (f"{ism} {familiya}")
# print(ism_familiya.capitalize())



# casefold()- kichik harfga o'zgartiradi
# ism = "SHUKURJON"
# familiya = "RAJABOVA"
# ism_familiya = (f"{ism} {familiya}")
# print(ism_familiya.casefold())
#
# meva = "OlMa"
# print(meva.casefold())



# center() - matnni markazga joylashtiradi
# ism = "SHUKURJON"
# familiya = "RAJABOVA"
# ism_familiya = (f"{ism} {familiya}")
# print(ism_familiya.center(40))
#
# car = "gentra"
# print(car.center(30))



# count() - so'zni qancha takrorlanganligini aniqlab beradi
# mevalar = "olma, anor, behi, olma, shaftoli, olma"
# a = mevalar.count('olma')
# print(a)
#
# mevalar = "olma, anor, behi, olma, shaftoli, olma, behi"
# a = mevalar.count('behi')
# print(a)



# encode()- utf8 formatlab beradi
# t = "Mening ismim Shukurjon😊"
# x = t.encode()
# print(x)
#
# a = "€ "
# x = a.encode()
# print(x)



# endswith() - so'z ohirida . yoki , kabi belgilar bor bo'lsa true qaytaradi
# a = "Salom."
# print(a.endswith('.'))
#
# a = "Salo,m"
# print(a.endswith(','))



# expandtabs()- \t ni tushurib qoldiradi va expandtabs(2) esa harflar orasida probel tashlaydi
# a = "S\ta\tl\to\tm"
# print(a.expandtabs(2))
#
# a = ("S\ta\t\tl\to\t\tm")
# print(a.expandtabs(0))



# find() - so'z oldida qancha probel borligini aniqlaydi
# b= "Hello World"
# print(b.find("World"))
#
b= "Salom mening ismim"
print(b.find("ismim"))



# format()	sonlarni double tipiga o'tqazadi. Satrda belgilangan qiymatlarni formatlaydi
# a = "Menda {price:.2f} ming pul bor."
# print(a.format(price = 250))
#
# a = "Menda {price:.2f} ming pul bor."
# print(a.format(price = 5255))



# format_map()-Satrda belgilangan qiymatlarni formatlaydi
# a = "Menda {price:.3f} ming pul bor."
# print(a.format(price = 250))
#
# a = "Menda {price:.2f} ming pul bor."
# print(a.format(price = 5255))



# index()- so'zni qaysi index dan boshlanganini ko'rsatadi. Masalan mening so'zni 6-indeksdan boshlangan
# bb = "Salom mening ismim Shukurjon"
# print(bb.index('mening'))
#
# bb = "Salom mening ismim Shukurjon"
# print(bb.index('Shukurjon'))



# isalnum() - satrda belgilar qatnashsa false qaytaradi
# matn = "Shukurjon15"
# print(matn.isalnum())
#
# matn = "Shukurjon/"
# print(matn.isalnum())



# isalpha() - faqat alifbodagi harflar qatnashsa true qaytaradi
# matn = "Shukurjon15"
# print(matn.isalpha())
#
# matn = "Shukurjon/"
# print(matn.isalpha())



# isascii() -
# matn = "Shukurjon15"
# print(matn.isascii())
#
# matn = "34347658762"
# print(matn.isascii())



# isdecimal()- satrda faqat raqamlar bo'lsa true qaytaradi
# matn = "345.00"
# print(matn.isdecimal())
#
# matn = "34347658762"
# print(matn.isdecimal())

#
#
# # isdigit()
# matn = "235"
# print(matn.isdigit())
#
# matn = "34347658762"
# print(matn.isdigit())



# isidentifier() - satrda faqat harf qatnashsa true qaytaradi
# bb = "Shukurjon"
# print(bb.isidentifier())
#
# bb = "Salom/."
# print(bb.isidentifier())



# islower() - agar satrdagii barcha belgiar kichik harf bo'lsa true qaytaradi
# bb = "shukurjon"
# print(bb.islower())
#
# bb = "salom/."
# print(bb.islower())



# isnumeric() - satrdagi barcha belgilar raqam bo'lsa true qaytaradi
# bb = "shukurjon"
# print(bb.isnumeric())
#
# bb = "35346"
# print(bb.isnumeric())



# isprintable()- satrdagi barcha belgilar bosma bo'lsa true qaytaradi
# bb = "shukurjon./"
# print(bb.isprintable())
#
# bb = "35346"
# print(bb.isprintable())



# isspace() - agar satr bo'sh bo'lsa true qaytaradi
# bb = "     "
# print(bb.isspace())
#
# bb = "35346"
# print(bb.isspace())



# istitle() - satrda qoidalarga rioya qilinsa true qaytaradi
# bb = "     "
# print(bb.istitle())
#
# bb = "Salom"
# print(bb.istitle())



# isupper() - satrdagi barcha belgilar katta harf bilan bo'lsa
# bb = "WEKJ2242 "
# print(bb.isupper())
#
# bb = "Salom, SHUKURJON"
# print(bb.isupper())



# join() - so'zlar orasiga belgilar qo'yadi
# abc = ("Shukurjon", "Rajabova")
# print("#".join(abc))
#
# abc = ("Shukurjon", "Rajabova", "Omonboy qizi")
# print(".".join(abc))



# ljust()- so'zlar orasiga probellar qo'yish
# matn = "banan"
# x = matn.ljust(10)
# print(x, "mening sevimli mevam.")
#
# matn = "banan"
# x = matn.ljust(40)
# print(x, "mening sevimli mevam.")



# lower() - satrdagi barcha belgilar kichik harf bilan yoziladi
# bb = "WEKJ2242 "
# print(bb.lower())
#
# bb = "Salom, SHUKURJON"
# print(bb.lower())



# lstrip()  - satrni chapga surib yozadi
# bb = "       salom      "
# print(bb.lstrip())
#
# bb = "           men"
# print(bb.lstrip())



# maketrans() - harfni o'zgartirish
# matn = "Salom Dunyo!"
# a = str.maketrans("n", "r")
# print(matn.translate(a))
#
# matn = "Salom Dunyo"
# a = str.maketrans("a", "o")
# print(matn.translate(a))



# partition() - Satrgadi so'zlarni belgilangan joydan" " ga olish
# a = "Men olmani yaxshi ko'raman"
# print(a.partition("yaxshi"))
#
# a = "Men olmani yaxshi ko'raman, kdhr sghkr"
# print(a.partition("yaxshi"))


