from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas
        self.__tesvik_primi = tesvik_primi

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    # Zam hakkını hesaplayan metot
    def zam_hakki(self):
        try:
            if self.__tecrube < 2:
                zam_miktari = self.__tesvik_primi
            elif 2 <= self.__tecrube <= 4 and self.__maas < 15000:
                zam_miktari = (self.__maas / self.__tecrube) * 5 + self.__tesvik_primi
            elif self.__tecrube > 4 and self.__maas < 25000:
                zam_miktari = (self.__maas / self.__tecrube) * 4 + self.__tesvik_primi
            else:
                zam_miktari = 0

            return zam_miktari
        except Exception as e:
            print("Bir hata oluştu:", str(e))
            return 0

    # Yeni maaşı hesaplayan metot
    def yeni_maas(self):
        try:
            zam_miktari = self.zam_hakki()
            yeni_maas = self.get_maas() + zam_miktari
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


