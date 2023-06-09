from Insan import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas

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

    # Zam hakkını hesaplayan fonksiyon
    def zam_hakki(self):
        try:
            if self.tecrube < 2:
                return 0
            elif 2 <= self.tecrube <= 4 and self.maas < 15000:
                return self.maas % self.tecrube
            elif self.tecrube > 4 and self.maas < 25000:
                return (self.maas % self.tecrube) / 2
            else:
                return 0
        except Exception as e:
            print("Bir hata oluştu:", str(e))

    def yeni_maas(self):
        try:
            zam_orani = self.zam_hakki()
            yeni_maas = self.get_maas + zam_orani
            return yeni_maas
        except Exception as e:
            print("Bir hata oluştu:", str(e))

    # Sınıfın metinsel temsilini döndüren metot
    def __str__(self):
        try:
            ad = self.get_ad() if self.get_ad() else "Bilinmiyor"
            soyad = self.get_soyad() if self.get_soyad() else "Bilinmiyor"
            yeni_maas = self.yeni_maas()

            return f"Ad: {ad}\nSoyad: {soyad}\nTecrübe: {self.__tecrube}\nYeni Maaş: {yeni_maas}"
        except Exception as e:
            print("Bir hata oluştu:", str(e))
            return ""  # Hata durumunda boş bir string döndürerek değer veriyoruz
