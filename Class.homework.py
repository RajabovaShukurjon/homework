# # 1
# class User:
#     def __init__(self, ismi, foydalanuvchi_ismi, email, telefon_r):
#         self.ismi = ismi
#         self.foy_ismi = foydalanuvchi_ismi
#         self.mail = email
#         self.telefon = telefon_r
#
#     def get_name(self):
#         """Userning ismini qaytaradi"""
#         return self.ismi
#
#
#     def get_username(self):
#         """Usernameni qaytaradi"""
#         return self.foy_ismi
#
#
#     def get_email(self):
#         return self.mail
#
#
#     def get_telefon(self):
#         return self.telefon
#
#     def get_info(self):
#         print(f"Foydalanuvchi: {self.foy_ismi}, ismi: {self.ismi}, email: {self.mail}, telefon: {self.telefon} ")
#
# user1 = User("Shukurjon", "RShukurjon", "rajabovashukurjon@gmail.com", +998976010615)
# user2 = User("Laylo", "laylooo6", "laylooo6@gmail.com", +998972012345)
#
# print(user1.get_name())
# print(user1.get_username())
# print(user2.get_email())
# print(user2.get_telefon())
# user2.get_info()



# 2
class Avto:
    def __init__(self, model, yil, yurgan_km, narx):
        self.model = model
        self.yil = yil
        self.yurgan_km = yurgan_km
        self.narx = narx

    def get_model(self):
        return self.model

    def get_yil(self):
        return self.yil

    def get_yurgan_km(self):
        return self.yurgan_km

    def get_narx(self):
        return self.narx


    def get_info(self):
        print(f"Model: {self.model}\nYil: {self.yil}\nYurgan_km: {self.yurgan_km} km\nNarx: ${self.narx}")

avto1 = Avto("Nexia", "2021", 30000, 5000)
avto2 = Avto("Malibu", "2020", 45000, 18000)
avto3 = Avto("Tracker", "2022", 20000, 15000)
avto2.get_info()

