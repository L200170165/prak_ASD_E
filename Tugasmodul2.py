class Pesan (object):
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumlahKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('kalimat mempunyai', len(self.teks), 'karakter')
    def perbarui(self, stringBaru):
        self.teks = stringBaru
    #Nomer 1A
    def apakahTerkandung(self,hurf):
        if hurf in self.teks:
            return True
        else:
            return False
    #Nomer 1B
    def hitungKonsonan(self):
        kon = "bcdfghjklmnpqrstvwxyzBCDFGHKLMNPQRSTVWXYZ"
        jum = 0
        for i in self.teks:
            if i in kon:
                jum += 1
        return jum

    #Nomer 1C
    def hitungVokal(self):
        vok = "aiueAIUEO"
        jum = 0
        for i in self.teks:
            if i in vok:
                jum += 1
        return jum

class Manusia(object):
    """class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku ",self.nama)
    def makan(self, s):
        print("Saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print("Saya baru saja latihan ", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n * 2

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku

    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            +". "+ self.uangSaku +' tiap bulannya.'
        return s

    #Nomer 2A
    def ambilKotaTinggal(self):
        return self.kotaTinggal

    #Nomer 2B
    def perbaruiKotaTinggal(self, ubah):
        self.kotaTinggal = ubah
    #Nomer 2C
    def tambahUangSaku(self, e):
        self.uangSaku += e
        return self.uangSaku

    #Nomer 4
    listKuliah = []
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)
    #Nomer 5
    def hapusKuliah(self, hapuslah):
        self.listKuliah.remove(hapuslah)

#Nomer3
print("\nNomer 3")
print("Silahkan Masukkan Data Mahasiswa Di bawah Ini :")
a = input("Nama Mahasiswa      : ")
b = input("NIM Mahasiswa       : ")
c = input("Asal Mahasiswa      : ")
d = input("Uang Saku Mahasiswa : ")
ma = Mahasiswa(a, b, c, d)
print(str(ma))

#Nomer 6
class SiswaSMA(Manusia):
    def __init__(self, nama, NIS, uangJajan, alamat):
        self.nama = nama
        self.nis = NIS
        self.uangJajan = uangJajan
        self.alamat = alamat
    def __str__(self):
        s = "Nama : " + str(self.nama) \
            + "NIS : " + str(self.nis) \
            + "Alamat : " + str(self.alamat)\
            + "Uang Jajan : " + str(self.uangJajan)
        return s

#Nomer 7
# Metoode atau state yang muncul berasal dari semua class baik Manusia, Mahasiswa, atau MhsTIF.
# Ini karena MhsTIF yang merupakan anak class dari Mahasiswa, dan itu membuat MhsTIF mewarisi
# semua properties dari Mahasiswa dan Manusia.
