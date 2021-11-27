import time
import random
import os

class Netflix():
    def __init__(self,netflix_durum="Kapalı",kisi_durumu="Kapalı"):
        self.netflix_durum=netflix_durum
        self.kisi_durumu=kisi_durumu
    def netflix_ac(self):
        if(self.netflix_durum=="Açık"):
            print("Zaten Açık")
        else:
            print("Netflix Açılıyor.")
            time.sleep(1)
            self.netflix_durum="Açık"
            print("Netflix Açıldı")
    def netflix_kapat(self):
        if(self.netflix_durum=="Kapat"):
            print("Zatan Kapalı")
        else:
            print("Netflix Kapanıyor.")
            time.sleep(3)
            self.netflix_durum="Kapalı"
            print("Netflix Kapandı")
    def __str__(self):
        return "Netflix Durum: {}\n".format(self.netflix_durum)
    def hesap_acik(self):
        if(self.kisi_durumu=="Açık"):
            print("Zaten Açık")
        elif(self.kisi_durumu=="Açık"):
            self.kisi_durumu = "Açık"
            print("Hesap Açıldı")

banner="""
    NETFLIX'E HOŞGELDİNİZ.
    
    1)Netflix Aç
    2)Netflix Kapat
    3)Netflix Durumu
    4)Hesaplar
    5)Bilgileri Tekrar Görmek İçin
    6)Çıkmak İçin 'q'
    7)Geliştirici
    """
print(banner)
netflix=Netflix()
while True:
    islem=input("İslem Seçiniz :")
    if (islem =="q"):
        print("Çıkış Yapılıyor.")
        time.sleep(2)
        break
    elif(islem=="1"):
        netflix.netflix_ac()
    elif(islem=="2"):
        netflix.netflix_kapat()
    elif(islem=="3"):
        print(netflix)
    elif(islem=="5"):
        print(banner)
    elif(islem=="7"):
        gokalp="""
    GÖKALP EROL
        """
        print(gokalp)
    elif(islem=="4"):
        banner1="""
    1-Mustafa
    2-Cem
    3-Kadir
        """
        print(banner1)
        secim=input("Seçim Yapınız :")
        if(secim=="1"):
            netflix.hesap_acik()
            banner2="""
    HESABINA HOŞGELDİN KULLANICI
    
    Nasıl Bir Film İzlemek İstersin?
    1-Macera
    2-Korku
    3-Dram
            """
            print(banner2)
            film=input("Hangisi : ")
            if(film=="1"):
                banner3="""
    MACERA FILM LİSTESİ
    1-Venom
    2-Spiderman
    3-Iron-Man  
                """
                print(banner3)
                film2=input("Hangi Film? : ")
                if(film2=="1"):
                    print("Film Açılıyor.")
                    time.sleep(2)
                    bilgi=input("Film başlamadan bilgi almak istermisiniz? '1'/'2': ")
                    if(bilgi=="1"):
                        banner4="""
                        Venom Filmi Hakkında Bilgi:
                        IMDB:6.7
                        Saat:2 saat 20 dakika
                        Başroller: Tom Hardy. Rolü : Eddie Brock / Venom.
                                   Michelle Williams. Rolü : Anne Weying.
                                   Riz Ahmed. Rolü : Dr. Carlton Drake
                        """
                        print(banner4)
                        time.sleep(10)
                        os.system("clear")
                        time.sleep(1)
                        print("Film Açıldı İyi Seyirler.")
                        os.system("figlet VENOM")
                    else:
                        print("Film Açıldı İyi Seyirler.")

                elif(film2=="2"):
                    print("Film Açılıyor.")
                    time.sleep(2)
                    bilgi1 = input("Film başlamadan bilgi almak istermisiniz? '1'/'2': ")
                    if (bilgi1 == "1"):
                        banner5 = """
                                            Spıderman Filmi Hakkında Bilgi:
                                            IMDB:7.3
                                            Saat:2 saat 30 dakika
                                            Başroller: Tobey Maguire. Rolü : Spiderman
                                                       Kirsten Dunst. Rolü : Mary Jane
                                                       James Franco . Rolü : New Goblin
                                            """
                        print(banner5)
                        time.sleep(10)
                        os.system("clear")
                        time.sleep(1)
                        print("Film Açıldı İyi Seyirler.")
                        os.system("figlet SPIDERMAN")
                    else:
                        print("Film Açıldı İyi Seyirler.")
                elif (film2 == "3"):
                    print("Film Açılıyor.")
                    time.sleep(2)
                    bilgi2 = input("Film başlamadan bilgi almak istermisiniz? '1'/'2': ")
                    if (bilgi2 == "1"):
                        banner6 = """
                                                            Iron-Man Filmi Hakkında Bilgi:
                                                            IMDB:7.9
                                                            Saat:2 saat 6 dakika
                                                            Başroller: Robert Downey Jr. Rolü : Iron-Man
                                                                       Jon Favreau. Rolü : Harold Hogan
                                                                       Gwyneth Paltrow. Rolü : Pepper Pots
                                                            """
                        print(banner6)
                        time.sleep(10)
                        os.system("clear")
                        time.sleep(1)
                        print("Film Açıldı İyi Seyirler.")
                        os.system("figlet IRON-MAN")
                    else:
                        print("Film Açıldı İyi Seyirler.")

            elif(film=="2"):
                banner3 = """
    DRAMA FILM LİSTESİ
    1-BIRDBOX
    2-ALIEN 
                                """
                print(banner3)
                filmsec=input("Film Seçiniz :")
                if(filmsec=="1"):
                    print("Film Açılıyor.")
                    bilgi1=input("Film Hakkında bilgi almak için '1'/'2' :")
                    if (bilgi1=="1"):
                        banner44 = """
                                                BIRDBOX Filmi Hakkında Bilgi:
                                                IMDB:6.7
                                                Saat:2 saat 20 dakika
                                                Başroller: Tom Hardy. Rolü : Eddie Brock / Venom.
                                                           Michelle Williams. Rolü : Anne Weying.
                                                           Riz Ahmed. Rolü : Dr. Carlton Drake
                                                """
                        print(banner44)
                        time.sleep(10)
                        os.system("clear")
                        time.sleep(1)
                        print("Film Açıldı İyi Seyirler.")
                        os.system("figlet BIRDBOX")
                    else:
                        print("Film Açıldı İyi Seyirler.")
                elif(filmsec=="2"):
                    print("Film Açılıyor.")
                    bilgi2 =input("Film Hakkında bilgi almak için '1'/'2' :")
                    if (bilgi2=="1"):
                        banner54 = """
                                                                        ALIEN Filmi Hakkında Bilgi:
                                                                        IMDB:6.7
                                                                        Saat:2 saat 20 dakika
                                                                        Başroller: Tom Hardy. Rolü : Eddie Brock / Venom.
                                                                                   Michelle Williams. Rolü : Anne Weying.
                                                                                   Riz Ahmed. Rolü : Dr. Carlton Drake
                                                                        """
                        print(banner54)
                        time.sleep(10)
                        os.system("clear")
                        time.sleep(1)
                        print("Film Açıldı İyi Seyirler.")
                        os.system("figlet ALIEN")
                    else:
                        print("Film Açıldı İyi Seyirler.")
            elif(film=="3"):
                print("Drama filmeri bakımdadır.")
                print("Geri Dönülüyor.")
                time.sleep(2)
        elif(secim=="2"):
            print("NETFLIX SUPPORT : Cem kullanıcısı bakımdadır.")
            print("Geri Dönülüyor")
            time.sleep(2)
        elif(secim=="3"):
            print("NETFLIX SUPPORT : Kadir kullanıcısı bakımdadır.")
            print("Geri Dönülüyor")
            time.sleep(2)

    else:
        print("Geçersiz İşlem")
