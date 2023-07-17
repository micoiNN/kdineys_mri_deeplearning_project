from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
import ekran_python
import nii_ekle_d
import degerlendirme_kismi
from PyQt5 import QtWidgets,QtGui
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

class Pencere(QDialog):
    def __init__(self):
        super(Pencere, self).__init__()
        self.baglanti()
        self.tanilar = ["Kist","Normal Sağlıklı","Taş","Tümör"]
        self.sorgu = None
        self.turkce_dil()
        self.deger = False

        self.ui.btn_kapa.clicked.connect(self.uygulama_kapat)
        self.ui.nii_katman.clicked.connect(self.ni_ekleme)
        self.ui.ni_onayla.clicked.connect(self.ni_onay)
        self.ui.ni_kaydet.clicked.connect(self.ni_kaydedilecek_yer)
        self.ui.bt_sec.clicked.connect(self.bt_sec_path)
        self.ui.isle_onay.clicked.connect(self.bt_isle)
        self.ui.d_yansi_2.clicked.connect(self.sayfa_1)
        self.ui.d_yansi.clicked.connect(self.sayfa_2)
        self.ui.turkce.clicked.connect(self.turkce_dil)
        self.ui.hasta_bilgi_kaydet.clicked.connect(self.hasta_kayit)
        self.ui.h_kaydet.clicked.connect(self.yapilacak_tahlil_islem)
        self.ui.english.clicked.connect(self.ingilizce_dil)

    def turkce_dil(self):
        self.ui.tumor_i_t.setText("Tümör bulunma ihtimali:")
        self.ui.kist_t.setText("Kist bulunma ihtimali:")
        self.ui.tas_t.setText("Taş bulunma ihtimali:")
        self.ui.normal_t.setText("Sağlıklı olma ihtimali:")
        self.ui.bt_sec.setText("BT Seç")
        self.ui.isle_onay.setText("İşle")
        self.ui.ni_kaydet.setText("kaydedilecek yeri seç")
        self.ui.ni_onayla.setText("Onayla")
        self.ui.nii_katman.setText(".nii dosya katmanlara ayir")
        self.ui.bt_semantic.setText("BT ile anlamsal bölütleme")
        self.ui.d_yansi.setText("Diğer yansı")
        self.ui.h_isim_t.setText("Hasta İsim Soy İsim")
        self.ui.h_yas_t.setText("Yaşı")
        self.ui.h_cinsiyet_t.setText("Cinsiyeti")
        self.ui.h_iletisim_t.setText("İletişim Bilgisi (Email)")
        self.ui.y_tahlil_t.setText("Yapılacak Tahliller ve İşlemler")
        self.ui.u_dil.setText("Uygulama Dili")
        self.ui.h_tani_oyku.setText("Tanı ve Hastanın Öyküsü")
        self.ui.d_yansi_2.setText("Diğer yansı")
        self.ui.h_kaydet.setText("İŞLE")
        self.ui.hasta_bilgi_kaydet.setText("Tüm bilgileri Kaydet")
        self.tanilar = ["Kist","Normal Sağlıklı","Taş","Tümör"]
        self.ui.muhtemel_text.setText("Muhtemel Tanı:")
        self.bilgilen = "Bilgilendirme"
        self.katman_1 = "CT KATMAN SAYISI:"
        self.katman_2 = "ŞURAYA KAYDEDİLDİ:"
        self.bt_isle_mesaj = "Eksik,hatalı yol veya BT seçimi yanlış olabilir"
        self.nii_mesaj = "kaydedilecek yer veya .nii dosyası hatalı"
        self.hasta_kayit_mesaj_1 = "Lütfen Boşluk bırakmayın"
        self.hasta_kayit_basari_mesaj = "İşlem gerçekleştirildi"
        self.hasta_kayit_id_mesaj = "id veya TCKN'de boşluk harf veya ondalıklı sayı yazmayın, tekrar deneyin"
        self._tahlil_1_mesaj = "Lütfen Tüm Boşlukları doldurun"
        self.yapilacak_tani_mesaj = "Lütfen Hasta bilgilerini eksiksiz kaydedin"
        self.hasta_eksiksiz_kaydet_mesaj = "Lütfen Hasta bilgilerini eksiksiz kaydedin"
        self.ui.tc_hasta.setText("Hasta TCKN")
        self.son_msg = "Tüm işlemler tamamlanmıştır bir sonraki hastaya geçiniz."
        self.eror_msg = "Lütfen daha önce Tomogrofiyi görüntüleyin"
        self.bilgi_son = "BT Yanlış seçilme işlemi yapılmış onu düzeltin"

        try:
            self.ui.t_tani.setText(self.tanilar[self.tani_s_deger])
        except:
            pass


    def ingilizce_dil(self):
        self.ui.tumor_i_t.setText("Probability of finding a tumor:")
        self.ui.kist_t.setText("Probability of cyst:")
        self.ui.tas_t.setText("The probability of finding a stone:")
        self.ui.normal_t.setText("Probability of being healthy:")
        self.ui.bt_sec.setText("CT Select")
        self.ui.isle_onay.setText("Process")
        self.ui.ni_kaydet.setText("choose where to save")
        self.ui.ni_onayla.setText("Accept")
        self.ui.nii_katman.setText("Layer .nii file")
        self.ui.bt_semantic.setText("Semantic segmentation with CT")
        self.ui.d_yansi.setText("Other half")
        self.ui.h_isim_t.setText("Patient Name Surname")
        self.ui.h_yas_t.setText("Age")
        self.ui.h_cinsiyet_t.setText("gender")
        self.ui.h_iletisim_t.setText("Contact Information (Email)")
        self.ui.y_tahlil_t.setText("Analysis and Transactions to be Made")
        self.ui.u_dil.setText("App Language")
        self.ui.h_tani_oyku.setText("Diagnosis and Patient's History")
        self.ui.d_yansi_2.setText("Other half")
        self.ui.h_kaydet.setText("PROCESS")
        self.ui.hasta_bilgi_kaydet.setText("Save all information")
        self.tanilar = ["Cyst","Normal Healthy","Stone","Tumor"]
        self.ui.muhtemel_text.setText("Probable Diagnosis:")
        self.bilgilen = "Information"
        self.katman_1 = "NUMBER OF CT LAYERS:"
        self.katman_2 = "SAVED HERE:"
        self.bt_isle_mesaj = "Missing, wrong path or wrong CT selection"
        self.nii_mesaj = "wrong save location or .nii file"
        self.hasta_kayit_mesaj_1 = "Please do not leave any spaces"
        self.hasta_kayit_basari_mesaj = "Transaction performed"
        self.hasta_kayit_id_mesaj = "Do not type spaces or decimals in id or TCKN, try again"
        self._tahlil_1_mesaj = "Please fill in all the blanks"
        self.yapilacak_tani_mesaj = "Please record patient information completely"
        self.hasta_eksiksiz_kaydet_mesaj = "Please record patient information completely"
        self.ui.tc_hasta.setText("Patient TCKN")
        self.son_msg = "All procedures are completed, go to the next patient."
        self.eror_msg = "Please view tomography before"
        self.bilgi_son = "CT Wrong Selected Fix it"

        try:
            self.ui.t_tani.setText(self.tanilar[self.tani_s_deger])
        except:
            pass
    def baglanti(self):
        self.ui = ekran_python.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

    def uygulama_kapat(self):
        self.close()

    def ni_ekleme(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        self.ni_path = path
    def ni_kaydedilecek_yer(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self)
        path = folderpath
        print(path)
        self.ni_kaydet_path = path

    def bilgilendirme(self,mesaj):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(str(f"{self.bilgilen}"))
        msg.setText(str(mesaj))
        msg.exec_()

    def ni_onay(self):
        try:
            if self.ni_path != [] and self.ni_kaydet_path != []:
                bilgi = nii_ekle_d.nii_to_jpg_fon(self.ni_path,self.ni_kaydet_path)
                mesaj = f"{self.katman_1} {bilgi[0]}\n{self.katman_2} {bilgi[1]}"
                self.bilgilendirme(mesaj)
            else:
               pass
        except:
            self.bilgilendirme(self.nii_mesaj)

    def bt_sec_path(self):
        filename = QFileDialog.getOpenFileName()
        self.bt_path = filename[0]

    def bt_isle(self):
        try:
                self.bilgi = degerlendirme_kismi.degerlendirme(self.bt_path)
                self.ui.t_ihtimal.setText(self.bilgi[3])
                self.ui.kist_ihtimal.setText(self.bilgi[0])
                self.ui.tas_ihtimal.setText(self.bilgi[2])
                self.ui.normal_ihtimal.setText(self.bilgi[1])

                self.tani_s_deger = self.bilgi[4]
                self.ui.t_tani.setText(self.tanilar[self.tani_s_deger])

                self.deger = True
                try:
                    self.ui.bt_2.setPixmap(QtGui.QPixmap(self.bt_path).scaled(590, 590, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                except:
                    pass

        except:
            self.ui.t_ihtimal.setText("")
            self.ui.kist_ihtimal.setText("")
            self.ui.tas_ihtimal.setText("")
            self.ui.normal_ihtimal.setText("")
            self.ui.t_tani.setText("")
            self.ui.bt_2.setPixmap(QtGui.QPixmap(f"{None}"))
            self.bilgilendirme(self.bt_isle_mesaj)
            self.deger = False




    def hasta_kayit(self):
        self.hasta_isim = self.ui.h_isim.text()
        self.hasta_yas = self.ui.h_yas.text()
        self.hasta_cinsiyet = self.ui.h_cinsiyet.text()
        self.hasta_email = self.ui.h_email.text()
        self.id_numarasi = self.ui.id_no.text()
        self.tc_hasta = self.ui.h_tc_yaz.text()

        self.islem = False

        if self.hasta_isim == "" or self.hasta_yas == "" or self.hasta_cinsiyet == "" or self.hasta_email =="":
            self.bilgilendirme(self.hasta_kayit_mesaj_1)
        else:
            try:
                self.id_numarasi = int(self.id_numarasi)
                self.tc_hasta = int(self.tc_hasta)

                self.islem = True
                self.bilgilendirme(self.hasta_kayit_basari_mesaj)

            except:
                self.bilgilendirme(self.hasta_kayit_id_mesaj)
                self.islem = False


    def yapilacak_tahlil_islem(self):
        try:
            if self.islem == True:
                try:
                    self.yapilacak_islemler = self.ui.y_islem.toPlainText()
                    self.hasta_oyku_tani = self.ui.h_oyku.toPlainText()

                    if self.yapilacak_islemler == "" or self.hasta_oyku_tani == "":
                        self.bilgilendirme(self._tahlil_1_mesaj)
                    else:
                        try:
                            if self.bilgi[5] != "" or self.bilgi[5] != " " or self.bilgi[5] != None or self.bilgi[5] != []:
                                if self.deger == True:
                                    self.bilgilendirme(self.son_msg)
                                    self.ui.t_ihtimal.setText("")
                                    self.ui.kist_ihtimal.setText("")
                                    self.ui.tas_ihtimal.setText("")
                                    self.ui.normal_ihtimal.setText("")
                                    self.ui.h_isim.setText("")
                                    self.ui.h_yas.setText("")
                                    self.ui.h_cinsiyet.setText("")
                                    self.ui.h_email.setText("")
                                    self.ui.id_no.setText("")
                                    self.ui.h_tc_yaz.setText("")
                                    self.ui.h_oyku.setText("")
                                    self.ui.y_islem.setText("")
                                    self.ui.t_tani.setText("")
                                    self.ui.bt_2.setPixmap(QtGui.QPixmap(f"{None}"))
                                else:
                                    self.bilgilendirme(self.bilgi_son)
                        except:
                            self.bilgilendirme(self.eror_msg)

                except:
                    pass
            else:
                self.bilgilendirme(self.yapilacak_tani_mesaj)
        except:
            self.bilgilendirme(self.hasta_eksiksiz_kaydet_mesaj)

    def sayfa_2(self):
        self.ui.page_2.resize(1050,650)
        self.ui.page_2.show()
        self.ui.page.close()

    def sayfa_1(self):
        self.ui.page.resize(1050,650)
        self.ui.page.show()
        self.ui.page_2.close()


app = QtWidgets.QApplication([])
acilma = Pencere()
acilma.show()
app.exec_()


