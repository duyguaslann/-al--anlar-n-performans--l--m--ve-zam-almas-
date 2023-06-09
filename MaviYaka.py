from Calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    # Zam hakkını hesaplayan metot
    def zam_hakki(self):
        try:
            if self.get_tecrube() < 2:
                zam_orani = self.__yipranma_payi * 10
            elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
                zam_orani = (self.get_maas() % self.get_tecrube()) / 2 + (self.__yipranma_payi * 10)
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                zam_orani = (self.get_maas() % self.get_tecrube()) / 3 + (self.__yipranma_payi * 10)
            else:
                zam_orani = 0

            return zam_orani
        except Exception as e:
            print("Bir hata oluştu:", str(e))
            return None

    # Yeni maaşı hesaplayan metot
    def yeni_maas(self):
        try:
            zam_orani = self.zam_hakki()
            yeni_maas = self.get_maas() + zam_orani
            if yeni_maas == self.get_maas():
                return self.get_maas()
            else:
                self.set_maas(yeni_maas)
                return yeni_maas

        except Exception as e:
            print("Bir hata oluştu:", str(e))
            return None

    # Sınıfın metinsel temsilini döndüren metot
    def __str__(self):
        try:
            ad = self.get_ad()
            soyad = self.get_soyad()
            yeni_maas = self.yeni_maas()

            if yeni_maas is not None:
                return f"Ad: {ad}\nSoyad: {soyad}\nTecrübe: {self.get_tecrube()}\nYeni Maaş: {yeni_maas:.2f}"
            else:
                return f"Ad: {ad}\nSoyad: {soyad}\nTecrübe: {self.get_tecrube()}\nYeni Maaş: Hesaplanamadı"
        except Exception as e:
            print("Bir hata oluştu:", str(e))
            return ""