import random
import time


class Kumanda():

    def __init__(self, tv_durum="Kapalı", tv_ses=0,         #Sınıfın kendine özel parametereleri
                                kanal_listesi=["TRT"],
                                kanal="TRT",
                                mod="Normal",
                                wifi = "Bağlı Değil",
                                dil = "Türkçe"):

        self.tv_durum = tv_durum

        self.tv_ses = tv_ses

        self.kanal_listesi = kanal_listesi

        self.kanal = kanal

        self.mod = mod

        self.wifi = wifi

        self.dil = dil

    def tv_ac(self):                                #Televizyonu açmak için kullanılan fonksiyon

        if (self.tv_durum == "Açık"):
            print("Televizyon zaten açık.\n")
        else:
            print("Televizyon açılıyor...\n")
            self.tv_durum = "Açık"

    def tv_kapat(self):                             #Televizyonu kapamak için kullanılan fonksiyon

        if (self.tv_durum == "Kapalı"):
            print("Televizyon zaten kapalı.\n")
        else:
            print("Televizyon kapatılıyor...\n")
            self.tv_durum = "Kapalı"

    def ses_ayari(self):                      #Televizyonun sesini ayarlar

        if (self.tv_durum == "Açık"):
            while True:
                cevap = input("Sesi azalt: '<'\nSesi artır: '>'\nÇıkış: 'çıkış'\n")

                if (cevap == "<"):
                    if (self.tv_ses != 0):
                        self.tv_ses -= 1
                        print("Ses:", self.tv_ses)

                elif (cevap == ">"):
                    if (self.tv_ses != 31):
                        self.tv_ses += 1
                        print("Ses:", self.tv_ses)

                else:
                    print("Ses:", self.tv_ses)
                    break
        else:
            print("Önce televizyonu aç.")

    def kanal_ekle(self, kanal_ismi):          #Televizona kanal ekler

        print("Kanal ekleniyor...")
        time.sleep(2)

        self.kanal_listesi.append(kanal_ismi)

        print("Kanal eklendi.\n")

    def rastgele_kanal(self):                  #Rastgele kanal değiştirir

        if (self.tv_durum == "Açık"):

            rastgele = random.randint(0, len(self.kanal_listesi) - 1)

            self.kanal = self.kanal_listesi[rastgele]

            print("Şu anki kanal:", self.kanal)
            print("")
        else:
            print("Önce televizyonu aç.")

    def __len__(self):                          #Televizyondaki kanalların sayısını döner
        return len(self.kanal_listesi)

    def __str__(self):                          #Televizyonun durumunu gösteren parametreler

        return "TV Durumu: {}\nTV Ses: {}\nKanal Listesi :{}\nİzlenen Kanal: {}\nMod: {}\nWifi: {}\n".format(self.tv_durum,
                                                                                                   self.tv_ses,
                                                                                                   self.kanal_listesi,
                                                                                                   self.kanal,
                                                                                                   self.mod,
                                                                                                   self.wifi)

    def mod_degistir(self):                     #Televizyonun görüntü modunu değiştirir

        if (self.tv_durum == "Açık"):
            while True:
                Mod = input("Normal Mod: '0'\nSinema Modu: '1'\nÇıkış: 'çıkış'\n")
                if(Mod == "0"):
                    if(self.mod == "Normal"):
                        print("Televizyon zaten Normal Modda\n")
                    else:
                        print("Normal Moda geçiliyor...\n")
                        self.mod = "Normal"
                        time.sleep(1)
                elif(Mod == "1"):
                    if(self.mod == "Sinema"):
                        print("Televizyon zaten Sinema Modunda.\n")
                    else:
                        print("Sinema Moduna geçiliyor...\n")
                        self.mod = "Sinema"
                        time.sleep(2)
                else:
                    print("Güncel Mod:", self.mod)
                    break
        else:
            print("Önce televizyonu aç.")

    def wifi_baglan(self):                      #Televizyonu internete bağlar
        if (self.tv_durum == "Açık"):
            seçim = input("İnternete Bağlan: '1'\nİnternet Değiştir: '2'\nİnterneti Kapat: '3'\n")

            while True:
                if(seçim == "1"):
                    if(self.wifi == "Bağlı"):
                        print("Televizyon zaten internete bağlı.")
                        break
                    else:
                        wifi_adi = input("İnternetinizin adını girin:")
                        sifre = input("Şifreyi girin:")
                        if(sifre == "1a2b3c4d"):
                            print("İnternete bağlanılıyor...\n")
                            time.sleep(4)
                            self.wifi = "Bağlı"
                            print("Bağlandığınız internet:", wifi_adi)
                            break
                        else:
                            print("Şifre yanlış.\n")
                            break

                elif(seçim == "2"):
                    wifi_adi = input("İnternetinizin adını girin:")
                    sifre = input("Şifreyi girin:")
                    if(sifre == "1a2b3c4d"):
                        print("İnternete bağlanılıyor...\n")
                        time.sleep(4)
                        self.wifi = "Bağlı"
                        print("Bağlandığınız internet:", wifi_adi)
                        break
                    else:
                        print("Şifre yanlış.\n")
                        break

                elif(seçim == "3"):
                    if(self.wifi == "Bağlı Değil"):
                        print("İnternet zaten kapalı.")
                        break
                    else:
                        self.wifi = "Bağlı Değil"
                        print("İnternet kapatılıyor...")
                        time.sleep(2)
                        break

                else:
                    print("Geçersiz işlem.")
                    break
        else:
            print("Önce televizyonu aç.")

    def dil_degistir(self):                         #Televizyonun dilini değiştirir
        if(self.tv_durum == "Açık"):
            print("Lütfen bir dil seçin:\n")
            tercih = input("Türkçe: 1\tİngilizce: 2\tJaponca: 3\tAlmanca: 4\tFransızca: 5\n")

            if(tercih == "1"):
                if (self.dil == "Türkçe"):
                    print("Dil zaten", self.dil, end=".\n")
                else:
                    self.dil = "Türkçe"
                    print("Dil ayarlanıyor...")
                    time.sleep(2)
                    print(self.dil, "diline ayarlandı.")

            elif(tercih == "2"):
                if (self.dil == "İngilizce"):
                    print("Dil zaten", self.dil, end=".\n")
                else:
                    self.dil = "İngilizce"
                    print("Dil ayarlanıyor...")
                    time.sleep(2)
                    print(self.dil, "diline ayarlandı.")

            elif(tercih == "3"):
                if(self.dil == "Japonca"):
                    print("Dil zaten",self.dil, end=".\n")
                else:
                    self.dil = "Japonca"
                    print("Dil ayarlanıyor...")
                    time.sleep(2)
                    print(self.dil, "diline ayarlandı.")

            elif (tercih == "4"):
                if (self.dil == "Almanca"):
                    print("Dil zaten", self.dil, end=".\n")
                else:
                    self.dil = "Almanca"
                    print("Dil ayarlanıyor...")
                    time.sleep(2)
                    print(self.dil, "diline ayarlandı.")

            elif (tercih == "5"):
                if (self.dil == "Fransızca"):
                    print("Dil zaten", self.dil, end=".\n")
                else:
                    self.dil = "Fransızca"
                    print("Dil ayarlanıyor...")
                    time.sleep(2)
                    print(self.dil, "diline ayarlandı.\n")

            else:
                print("Geçersiz işlem.\n")
        else:
            print("Önce televizyonu aç.\n")


kumanda = Kumanda()

print("""
Televizyon Uygulaması

1. TV Aç

2. TV Kapa

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sayısını Öğren

6. Rastgele Kanal Değiştir

7. Mod Değiştir

8. İnternete Bağlan

9. Dil

10.Televizyon Bilgileri

Çıkış: 'q' ya bas
""")

while True:                             #Seçim işlemleri buradan yürütülür
    işlem = input("İşlemi Seçiniz:")

    if (işlem == "q"):
        print("Çıkış yapılıyor...")
        time.sleep(2)
        break

    elif (işlem == "1"):
        kumanda.tv_ac()

    elif (işlem == "2"):
        kumanda.tv_kapat()

    elif (işlem == "3"):
        kumanda.ses_ayari()

    elif (işlem == "4"):

        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin:")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)


    elif (işlem == "5"):
        print("Kanal Sayısı:", len(kumanda))
        print("")

    elif (işlem == "6"):
        kumanda.rastgele_kanal()

    elif (işlem == "7"):
        kumanda.mod_degistir()

    elif (işlem == "8"):
        kumanda.wifi_baglan()

    elif (işlem == "9"):
        kumanda.dil_degistir()

    elif (işlem == "10"):
        print(kumanda)

    else:
        print("Geçersiz İşlem.")