import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QLineEdit

class Arayuz(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Online Eğitim Platformu")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Hoş Geldiniz yazısını oluştur
        welcome_text = "<font color='red'><b>HOŞ GELDİNİZ!</b></font>"

        # QLabel oluştur
        self.label = QLabel()
        self.label.setText(welcome_text)
        self.layout.addWidget(self.label)

        # Kurs bilgisini göstermek için bir QLabel oluşturalım
        self.kurslar_label = QLabel()
        self.layout.addWidget(self.kurslar_label)

        # Öğrenci verilerini saklamak için bir liste oluşturalım
        self.ogrenciler = []

        self.kurslar = {
            "Python Programlama": {
                "İçerik": "Python programlama dilinin temelleri",
                "Süre": "4 hafta",
                "Fiyat": "5000 TL",
                "Eğitmen": {
                    "Adı": "Ahmet Yılmaz",
                    "Uzmanlık Alanı": "Yazılım Geliştirme",
                    "Akademik Derece": "Yüksek Lisans",
                    "İş Deneyimi": "5 yıl"
                },
                "Öğrenci Sayısı": 0
            },
            "Veri Bilimi": {
                "İçerik": "Veri bilimi ve yapay zeka",
                "Süre": "8 hafta",
                "Fiyat": "3500 TL",
                "Eğitmen": {
                    "Adı": "Fatma Demir",
                    "Uzmanlık Alanı": "Veri Analizi",
                    "Akademik Derece": "Doktora",
                    "İş Deneyimi": "7 yıl"
                },
                "Öğrenci Sayısı": 0
            },
            "Yapay Zeka": {
                "İçerik": "Yapay zeka ve makine öğrenmesi",
                "Süre": "12 hafta",
                "Fiyat": "4000 TL",
                "Eğitmen": {
                    "Adı": "Mehmet Can",
                    "Uzmanlık Alanı": "Derin Öğrenme",
                    "Akademik Derece": "Doktora",
                    "İş Deneyimi": "6 yıl"
                },
                "Öğrenci Sayısı": 0
            },
            "Web Geliştirme": {
                "İçerik": "Web geliştirme ve tasarımı",
                "Süre": "6 hafta",
                "Fiyat": "3500 TL",
                "Eğitmen": {
                    "Adı": "Ayşe Kaya",
                    "Uzmanlık Alanı": "Frontend Geliştirme",
                    "Akademik Derece": "Lisans",
                    "İş Deneyimi": "4 yıl"
                },
                "Öğrenci Sayısı": 0
            }
        }

        # Kurs bilgilerini göstermek için metodu çağır
        self.goster_kurs_bilgileri()

        # Kayıtlı öğrencileri göstermek için düğme oluştur
        self.kayitli_ogrenciler_dugme = QPushButton("Kayıtlı Öğrencileri Göster")
        self.kayitli_ogrenciler_dugme.clicked.connect(self.kayitli_ogrencileri_goster)
        self.layout.addWidget(self.kayitli_ogrenciler_dugme)

    def goster_kurs_bilgileri(self):
        # Kurs bilgilerini QLabel'e yaz
        kurslar_text = "<b>Kurslar:</b><br>"
        for kurs_adi, bilgiler in self.kurslar.items():
            kurs_button = QPushButton(f"{kurs_adi}")
            kurs_button.clicked.connect(lambda _, kurs=kurs_adi: self.detaylari_goster(kurs))
            self.layout.addWidget(kurs_button)
        self.kurslar_label.setText(kurslar_text)

    def detaylari_goster(self, kurs_adi):
        bilgiler = self.kurslar[kurs_adi]
        detaylar = f"<b>İçerik:</b> {bilgiler['İçerik']}<br>"
        detaylar += f"<b>Süre:</b> {bilgiler['Süre']}<br>"
        detaylar += f"<b>Fiyat:</b> {bilgiler['Fiyat']}<br>"
        detaylar += f"<b>Eğitmen Adı:</b> {bilgiler['Eğitmen']['Adı']}<br>"
        detaylar += f"<b>Uzmanlık Alanı:</b> {bilgiler['Eğitmen']['Uzmanlık Alanı']}<br>"
        detaylar += f"<b>Akademik Derece:</b> {bilgiler['Eğitmen']['Akademik Derece']}<br>"
        detaylar += f"<b>İş Deneyimi:</b> {bilgiler['Eğitmen']['İş Deneyimi']}<br>"
        detaylar += f"<b>Kayıtlı Öğrenci Sayısı:</b> {bilgiler['Öğrenci Sayısı']}<br>"

        dialog = QDialog(self)
        dialog.setWindowTitle(f"{kurs_adi} Kursu Detayları")
        dialog.setGeometry(200, 200, 400, 300)
        dialog_layout = QVBoxLayout()
        dialog.setLayout(dialog_layout)
        detaylar_label = QLabel(detaylar)
        dialog_layout.addWidget(detaylar_label)
        
        # Kayıt Ol butonunu ekle
        kayit_ol_button = QPushButton("Kayıt Ol")
        kayit_ol_button.clicked.connect(lambda _, kurs=kurs_adi: self.kayit_ol(kurs))
        dialog_layout.addWidget(kayit_ol_button)
        
        dialog.exec_()

    def kayit_ol(self, kurs_adi):
        # Kullanıcıdan veri girişi için bir pencere oluştur
        kayit_dialog = QDialog(self)
        kayit_dialog.setWindowTitle("Kayıt Ol")
        kayit_dialog.setGeometry(200, 200, 300, 200)
        kayit_layout = QVBoxLayout()
        kayit_dialog.setLayout(kayit_layout)
        
        # Kullanıcı veri girişi alanlarını oluştur
        ad_soyad_label = QLabel("Adı Soyadı:")
        self.ad_soyad_input = QLineEdit()
        kayit_layout.addWidget(ad_soyad_label)
        kayit_layout.addWidget(self.ad_soyad_input)
        
        email_label = QLabel("E-posta:")
        self.email_input = QLineEdit()
        kayit_layout.addWidget(email_label)
        kayit_layout.addWidget(self.email_input)
        
        telefon_label = QLabel("Telefon Numarası:")
        self.telefon_input = QLineEdit()
        kayit_layout.addWidget(telefon_label)
        kayit_layout.addWidget(self.telefon_input)
        
        dogum_label = QLabel("Doğum Tarihi:")
        self.dogum_input = QLineEdit()
        kayit_layout.addWidget(dogum_label)
        kayit_layout.addWidget(self.dogum_input)
        
        # Kayıt Ol butonunu ekle
        kaydet_button = QPushButton("Kaydet")
        kaydet_button.clicked.connect(lambda: self.kaydet(kurs_adi))
        kayit_layout.addWidget(kaydet_button)
        
        kayit_dialog.exec_()
    
    def kaydet(self, kurs_adi):
        # Kullanıcının girdiği verileri al
        ad_soyad = self.ad_soyad_input.text()
        email = self.email_input.text()
        telefon = self.telefon_input.text()
        dogum = self.dogum_input.text()
        
        # Doğum tarihini uygun formata dönüştür
        dogum = self.format_dogum_tarihi(dogum)
        
        # Kullanıcının girdiği verileri sakla
        ogrenci_bilgisi = {
            "Adı Soyadı": ad_soyad,
            "E-posta": email,
            "Telefon Numarası": telefon,
            "Doğum Tarihi": dogum,
            "Kurs Adı": kurs_adi
        }
        self.ogrenciler.append(ogrenci_bilgisi)
        
        # Burada verileri kaydetme işlemi gerçekleştirilebilir.
        print("Kaydedilen Veriler:")
        print("Adı Soyadı:", ad_soyad)
        print("E-posta:", email)
        print("Telefon Numarası:", telefon)
        print("Doğum Tarihi:", dogum)
        print("Kurs Adı:", kurs_adi)
        print("Öğrenciler:", self.ogrenciler)

    def kayitli_ogrencileri_goster(self):
        # Kayıtlı öğrencilerin listesini göstermek için bir pencere oluştur
        ogrenciler_dialog = QDialog(self)
        ogrenciler_dialog.setWindowTitle("Kayıtlı Öğrenciler")
        ogrenciler_dialog.setGeometry(200, 200, 400, 300)
        ogrenciler_layout = QVBoxLayout()
        ogrenciler_dialog.setLayout(ogrenciler_layout)

        # Kayıtlı öğrencilerin bilgilerini QLabel'e yaz
        ogrenciler_text = "<b>Kayıtlı Öğrenciler:</b><br>"
        for ogrenci in self.ogrenciler:
            ogrenci_bilgisi = f"<b>Adı Soyadı:</b> {ogrenci['Adı Soyadı']}<br>"
            ogrenci_bilgisi += f"<b>E-posta:</b> {ogrenci['E-posta']}<br>"
            ogrenci_bilgisi += f"<b>Telefon Numarası:</b> {ogrenci['Telefon Numarası']}<br>"
            ogrenci_bilgisi += f"<b>Doğum Tarihi:</b> {ogrenci['Doğum Tarihi']}<br>"
            ogrenci_bilgisi += f"<b>Kurs Adı:</b> {ogrenci['Kurs Adı']}<br><br>"
            ogrenciler_text += ogrenci_bilgisi

        ogrenciler_label = QLabel(ogrenciler_text)
        ogrenciler_layout.addWidget(ogrenciler_label)

        ogrenciler_dialog.exec_()

    def format_dogum_tarihi(self, tarih):
        # Doğum tarihini uygun formata dönüştür
        # Girdi formatı: gg.aa.yyyy
        # Çıktı formatı: yyyy-aa-gg
        gun, ay, yil = tarih.split('.')
        return f"{yil}-{ay.zfill(2)}-{gun.zfill(2)}"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    arayuz = Arayuz()
    arayuz.show()
    sys.exit(app.exec_())




