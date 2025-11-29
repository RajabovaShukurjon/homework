class Mahsulot:
    def __init__(self, id, nomi, narxi, soni, rating):
        self.id = id
        self.nomi = nomi
        self.narxi = narxi
        self.soni = soni
        self.rating = rating

    def get_mah_mal_chiqarish(self, mah_mal_chiqarish):
        return mah_mal_chiqarish

    def get_narx_yangilash(self, narx_yangilash):
        return narx_yangilash


class Savat:
    def __init__(self, mahsulotlar, umumiy_narx):
        self.mahsulotlar = mahsulotlar
        self.umumiy_narx = umumiy_narx

    def get_mahsulot_qoshish(self, mahsulot_qoshish):
        return mahsulot_qoshish

    def get_mahsulot_olib_tashlash(self, mahsulot_olib_tashlash):
        return mahsulot_olib_tashlash

    def get_savat_tozalash(self, savat_tozalash):
        return savat_tozalash

    def get_umumiy_narxni_hisoblash(self, umumiy_narxni_hisoblash):
        return umumiy_narxni_hisoblash

    def get_bosh_yoki_b_emas(self, bosh_yoki_b_emas):
        return bosh_yoki_b_emas

