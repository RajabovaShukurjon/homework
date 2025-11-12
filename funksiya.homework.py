# 1
# def yil_hisobla():
#     """Foydalanuvchidan yoshini so'rab yilini hisoblovchi funksiya"""
#     ismi = input("Ismingizni kiriting:")
#     yosh = int(input("Yoshingizni kiriting:"))
#     tugilgan_yili = 2025 - yosh
#     print(f"Siz {tugilgan_yili}-yilda tug'ilgansiz.")
# yil_hisobla()



# 2
# def kvadrat_kubi():
#     """Foydalanuvchidan son so'rab kvadrati va kubini hisoblovchi funksiya"""
#     son = int(input("Son kiriting:"))
#     son_kvadrati = son**2
#     son_kubi = son**3
#     print(f"{son} ning kvadrati:{son_kvadrati} \n{son} ning kubi:{son_kubi}")
# kvadrat_kubi()


# 3
# def juft_toq():
#     """Foydalanuvchidan son so'rab juft yoki toqligini hisoblovchi funksiya"""
#     son = int(input("Son kiriting:"))
#     if son % 2 == 0:
#         print(f"{son} juft son")
#     else:
#         print(f"{son} toq son")
# juft_toq()



# 4_
# def sonlar_tengligi():
#     son1 = int(input("Birinchi sonni kiriting:"))
#     son2 = int(input("Ikkinchi sonni kiriting:"))
#     if son1 == son2:
#         print("Sonlar teng")
#
# sonlar_tengligi()



# 5
# def xy():
#     """x ning y darajasini hisoblash funksiyasi"""
#     son1 = int(input("x ni kiriting:"))
#     son2 = int(input("y ni kiriting:"))
#     son_darajasi = son1 ** son2
#     print(f"{son1} ning {son2}-darajasi {son_darajasi} ga teng ")
# xy()



# 6
# def xy(son2 = 2):
#     """x ning y darajasini hisoblash funksiyasi"""
#     son1 = int(input("x ni kiriting:"))
#     son_darajasi = son1 ** son2
#     print(f"{son1} ning {son2}-darajasi {son_darajasi} ga teng ")
# xy()




# 7
def bolinish_tekshir():
    son = int(input("Son kiriting: "))
    for i in range(2, 11):
        if son % i == 0:
            print(f"{son} soni {i} ga qoldiqsiz bo‘linadi.")
        else:
            print(f"{son} soni {i} ga qoldiqsiz bo‘linmaydi.")
bolinish_tekshir()
