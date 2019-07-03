from remake import mahasiswa
from test import urut

mhs1 = mahasiswa("Aliando", 123, "Solo", 25000)
mhs2 = mahasiswa("Imron", 124, "Medan", 36000)
mhs3 = mahasiswa("Supriono", 125, "Wakanda", 91000)
mhs4 = mahasiswa("Stark", 126, "Bekonang", 85500)
mhs5 = mahasiswa("Burhan", 127, "Vormir", 97000)

nimMhs = [mhs1.NIM, mhs2.NIM, mhs3.NIM, mhs4.NIM, mhs5.NIM]
usMhs = [mhs1.us, mhs2.us, mhs3.us, mhs4.us, mhs5.us]

a = urut(nimMhs)
b = urut(usMhs)

a.printMerge(nimMhs)
b.printMerge(usMhs)

a.printQuick(nimMhs)
b.printQuick(usMhs)
