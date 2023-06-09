import pandas as pd
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

calisan1 = Calisan("11111111111", "Enes", "Yağmur",35,"Erkek", "Türk", "Teknoloji", 12, 22000)
calisan2 = Calisan("22222222222", "Sophia", "Black", 28, "Kadın", "Yunan", "Finans", 7, 10000)
calisan3 = Calisan("33333333333", "Diego", "Leonardo",40,"Erkek", "İtalyan", "Hizmet",28, 22000)


mavi_yaka1 = MaviYaka("44444444444", "Canan", "Aydın", 30, "Kadın", "Türk", "Üretim", 2, 14000, 0.2)
mavi_yaka2 = MaviYaka("55555555555", "Kayra", "Aktaş", 40, "Erkek", "Türk", "Lojistik", 5, 10000, 0.5)
mavi_yaka3 = MaviYaka("66666666666", "Berna", "Şimşek", 26, "Kadın", "Türk", "Satış", 2, 16500, 0.3)

beyaz_yaka1 = BeyazYaka("77777777777", "Can", "Kaçar", 35, "Erkek", "Türk", "Muhasebe", 10, 30000, 500)
beyaz_yaka2 = BeyazYaka("88888888888", "Irmak", "Aydın", 30, "Kadın", "Türk", "Pazarlama", 6, 28000, 2500)
beyaz_yaka3 = BeyazYaka("99999999999", "Hakan", "Deniz", 40, "Erkek", "Türk", "İnsan Kaynakları", 12, 32000, 1000)

print("\n" * 1)
data = {
    "Nesne Türü": ["Çalışan", "Çalışan", "Çalışan",
                   "Mavi Yaka", "Mavi Yaka", "Mavi Yaka",
                   "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],
    "TC No": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(),
              mavi_yaka1.get_tc_no(), mavi_yaka2.get_tc_no(), mavi_yaka3.get_tc_no(),
              beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no(), beyaz_yaka3.get_tc_no()],
    "Ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(),
            mavi_yaka1.get_ad(), mavi_yaka2.get_ad(), mavi_yaka3.get_ad(),
            beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()],
    "Soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(),
               mavi_yaka1.get_soyad(), mavi_yaka2.get_soyad(), mavi_yaka3.get_soyad(),
               beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad(), beyaz_yaka3.get_soyad()],
    "Yaş": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(),
             mavi_yaka1.get_yas(), mavi_yaka2.get_yas(), mavi_yaka3.get_yas(),
             beyaz_yaka1.get_yas(), beyaz_yaka2.get_yas(), beyaz_yaka3.get_yas()],
    "Cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(),
                  mavi_yaka1.get_cinsiyet(), mavi_yaka2.get_cinsiyet(), mavi_yaka3.get_cinsiyet(),
                  beyaz_yaka1.get_cinsiyet(), beyaz_yaka2.get_cinsiyet(), beyaz_yaka3.get_cinsiyet()],
    "Uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(),
               mavi_yaka1.get_uyruk(), mavi_yaka2.get_uyruk(), mavi_yaka3.get_uyruk(),
               beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk(), beyaz_yaka3.get_uyruk()],
    "Sektör": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(),
                mavi_yaka1.get_sektor(), mavi_yaka2.get_sektor(), mavi_yaka3.get_sektor(),
                beyaz_yaka1.get_sektor(), beyaz_yaka2.get_sektor(), beyaz_yaka3.get_sektor()],
    "Tecrübe": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(),
                 mavi_yaka1.get_tecrube(), mavi_yaka2.get_tecrube(), mavi_yaka3.get_tecrube(),
                 beyaz_yaka1.get_tecrube(), beyaz_yaka2.get_tecrube(), beyaz_yaka3.get_tecrube()],
    "Maaş": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(),
              mavi_yaka1.get_maas(), mavi_yaka2.get_maas(), mavi_yaka3.get_maas(),
              beyaz_yaka1.get_maas(), beyaz_yaka2.get_maas(), beyaz_yaka3.get_maas()],
    "Yıpranma Payı": [0, 0, 0,
                      mavi_yaka1.get_yipranma_payi(), mavi_yaka2.get_yipranma_payi(), mavi_yaka3.get_yipranma_payi(),0,0,0],
    "Teşvik Prim": [0, 0, 0, 0, 0, 0, beyaz_yaka1.get_tesvik_primi(), beyaz_yaka2.get_tesvik_primi(), beyaz_yaka3.get_tesvik_primi()],
}

# a)Tüm sütunları yan yana yazdırmak için seçeneği ayarla
pd.set_option('display.expand_frame_repr', False)
df = pd.DataFrame(data)
df.index += 1  # Indeksi 1'den başlayacak şekilde güncelle
print(df)
df = pd.DataFrame(data)

print("\n" * 1)

# b)Gruplama yaparak tecrübe ve yeni maaş ortalamalarını hesapla
df['Yeni Maaş'] = df['Maaş'] + df['Yıpranma Payı'] * df['Maaş'] + df['Teşvik Prim']
grouped = df.groupby("Nesne Türü").agg({"Tecrübe": "mean", "Yeni Maaş": "mean"})

grouped = grouped.reindex(["Çalışan", "Mavi Yaka", "Beyaz Yaka"])
print(grouped)

print("\n" * 1)

# c)Maaşı 15000 TL üzerinde olanların sayısını bul
maas_ust_limit = 15000
maas_ust_limit_uzeri = df[df["Maaş"] > maas_ust_limit].shape[0]
print("Maaşı 15000 TL üzerinde olan kişilerin sayısı:", maas_ust_limit_uzeri)

print("\n" * 1)

# d)Yeni maaşa göre DataFrame'i küçükten büyüğe sırala
df['Yeni Maaş'] = df['Maaş'] + df['Yıpranma Payı'] * df['Maaş'] + df['Teşvik Prim']
df_sorted = df.sort_values(by="Yeni Maaş")
df_sorted.index = df_sorted.index + 1
print(df_sorted)


print("\n" * 1)

# e)Tecrübesi 3 seneden fazla olan Beyaz yakalıları bul
beyaz_yaka_filtre = (df["Nesne Türü"] == "Beyaz Yaka") & (df["Tecrübe"] > 3)
beyaz_yaka_uzmanlar = df[beyaz_yaka_filtre]
print(beyaz_yaka_uzmanlar)

print("\n" * 1)

# f)Yeni maaşı 10000 TL üzerinde olanları filtrele
filtered_df = df[df['Yeni Maaş'] > 10000].iloc[1:5, [1, 9]]
print(filtered_df)


print("\n" * 1)

# g)Var olan DataFrame’den ad, soyad, sektör ve yeni maaşı içeren yeni bir DataFrame elde ediniz ve yazdırınız.
df['Yeni Maaş'] = df['Maaş'] + df['Yıpranma Payı'] * df['Maaş'] + df['Teşvik Prim']
new_df = df[['Ad', 'Soyad', 'Sektör', 'Yeni Maaş']]
new_df.index = new_df.index + 1
print(new_df)

