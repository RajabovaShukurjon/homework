class Shaxs:
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh

    def get_info(self):
        return f"{self.ism} {self.familiya}, {self.yosh} yosh"



class Fan:
    def __init__(self, nomi):
        self.nomi = nomi

    def get_nomi(self):
        return self.nomi



class Talaba(Shaxs):
    def __init__(self, ism, familiya, yosh):
        super().__init__(ism, familiya, yosh)
        self.fanlar = []

    def fanga_yozil(self, fan_obj):
        self.fanlar.append(fan_obj)

    def remove_fan(self, fan_obj):
        if fan_obj not in self.fanlar:
            return "Siz bu fanga yozilmagansiz"
        self.fanlar.remove(fan_obj)

    def get_info(self):
        fanlar = ", ".join([fan.nomi for fan in self.fanlar]) if self.fanlar else "Fan yo‘q"
        return f"Talaba: {self.ism} {self.familiya}, {self.yosh} yosh. Fanlar: {fanlar}"




class Professor(Shaxs):
    def __init__(self, ism, familiya, yosh, kafedra):
        super().__init__(ism, familiya, yosh)
        self.kafedra = kafedra

    def get_info(self):
        return f"Professor: {self.ism} {self.familiya}, {self.yosh} yosh. Kafedra: {self.kafedra}"


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, yosh, username):
        super().__init__(ism, familiya, yosh)
        self.username = username

    def get_info(self):
        return f"Foydalanuvchi: {self.username} ({self.ism} {self.familiya})"




class Admin(Foydalanuvchi):
    def ban_user(self, user):
        print(f"Foydalanuvchi bloklandi: {user.username}")




matematika = Fan("Matematika")
informatika = Fan("Informatika")
fizika = Fan("Fizika")

talaba1 = Talaba("Ali", "Valiyev", 20)

talaba1.fanga_yozil(matematika)
talaba1.fanga_yozil(informatika)

print(talaba1.get_info())

print(talaba1.remove_fan(fizika))

talaba1.remove_fan(informatika)

print(talaba1.get_info())


prof = Professor("Shukurjon", "Rajabova", 19, "Telekommunikatsiya")
print(prof.get_info())


user1 = Foydalanuvchi("Laylo", "Tojiboyeva", 19, "Telekommunikatsiya")


admin = Admin("Shukurjon", "Rajabova", 19, "Shukurjon15")
admin.ban_user(user1)
