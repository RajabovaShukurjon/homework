class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.__passport = passport
        self.__tyil = tyil

        def get_passport(self):
            return self.__passport

        def get_tyil(self):
            return self.__tyil




class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.__idraqam = idraqam
        self.bosqich = 1
        self.__manzil = manzil

    def get_id(self):
        return self.__idraqam

    def get_bosqich(self):
        return self.bosqich

    def get_manzil(self):
        return self.__manzil


    # @classmethod
    # def get_

talaba1 = Talaba("Shukurjon", "Rajabova", "AD1234567", 2006, "asfg4676gf76", "Xorazm viloyati")
talaba1.add_idraqam()