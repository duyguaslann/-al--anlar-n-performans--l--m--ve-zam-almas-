from Insan import Insan
class Issiz:
    def __init__(self, ad, soyad, tecrube):
        self.ad = ad
        self.soyad = soyad
        self.tecrube = tecrube
        self.__statuler = {
            "mavi yaka": 0.20,
            "beyaz yaka": 0.35,
            "yönetici": 0.45
        }
        self.__statu = None
        self.statu_bul()

    # En uygun statüyü belirleyen metot
    def get_statu(self):
        return self.__statu

    def set_statu(self, statu):
        self.__statu = statu

    def statu_bul(self):
        max_etki = 0
        for statu, etki in self.__statuler.items():
            try:
                etki_tahmini = self.tecrube * etki
                if etki_tahmini > max_etki:
                    max_etki = etki_tahmini
                    self.set_statu(statu)
            except TypeError:
                print("Geçersiz tecrube değeri. Tecrube, sayısal bir değer olmalıdır.")
                self.set_statu(None)

    # Sınıfın metinsel temsilini döndüren metot
    def __str__(self):
        return f"{self.ad} {self.soyad} için en uygun statü: {self.get_statu()}"

issiz1 = Issiz("Derya","Durmaz",10)
print(issiz1.get_statu())

issiz2= Issiz("Leyla","Altan",2)
print(issiz2.get_statu())
