class manusia(object):
    """ This is class Manusia dengan inisiasi 'Nama' """
    keadaan='Lapar'
    def __init__(self,nama):
        self.nama=nama
    def ucap(self):
        print("Hallo my name is: ",self.nama)
    def olah(self,k):
        print('Saya habis',k)
        self.keadaan='Lapar'
    def makan(self,s):
        print("Saya baru saja makan ",s)
        self.keadaan='Kenyang'
    def kali(self,n):
        return n*2
