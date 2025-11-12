#################1###################
# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
# for pochta in pochtalar:
#     if "@" in pochta:
#         print(f"To'g'ri email: {pochta}")
#     else:
#         print(f"Noto'g'ri email: {pochta}")



# ###############3##################
# ob_havo = [20 ,22, 19, 24, 25, 23, 21]
# kunlar = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
# ortacha =sum(ob_havo)/len(ob_havo)
# print(f"O'rtacha harorat: {ortacha}")
#
# for kunlar,harorat in zip(kunlar,ob_havo):
#     if harorat >= 22:
#         print(f"{kunlar}: {harorat} Iliq kun")
#     else:
#         print(f"{kunlar}: {harorat} Salqin kun")


###################4####################
# mavjud_taomlar = ["Osh", "Shashlik", "Manti", "Lag'mon" ]
# ovqat = input("Buyurtmangizni kiriting:")
# if ovqat.title() in mavjud_taomlar:
#     print("Buyurtmangiz qabul qilindi😊")
# else:
#     print("Kechirasiz, bunday taom yo'q😒")



######################5####################
# yoshlari = [16, 21, 17 , 30, 25]
# for yosh in yoshlari:
#     print(f"Yosh chegarasiga yetmagan: {yosh}") if yosh<18 else print(f"Xush kelibsiz: {yosh}" )



###################6###################
# xabarlar=["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
# for xabar in xabarlar:
#     if xabar == xabarlar[1]:
#         print(f"{xabar}: Telefoningizni quvvatlang")
#     else:
#         print(f"{xabar}: Quvvatlash kerak emas")


##################7################
# fayllar = str([ "kitob.jpg", "ko'k jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"])
# musiqalar=[]
# rasmlar=[]
# for i in fayllar:
#     if i.find('.mp3') != -1:
#         musiqalar.append(i)
#     else:
#         rasmlar.append(i)
# print(musiqalar)
# print(rasmlar)