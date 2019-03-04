#nomer 1
def cetakSiku(x):
    for i in range(x):
        for j in range(i+1):
            print('*', end='')
        print()

cetakSiku(1)

#nomer 2
def persegi(x,y):
    for i in range(x):
        if i == 0 or i == x-1:
            print('#'*x)
        else:
            a = x -y
            print("$"+ " "*(x-2)+"$")

persegi(4,5)

#nomer 3
def hurufVokal(nama):
    vok = 0
    kos = 0
    x = "aiueoAIUEO"
    for car in nama.lower():
        if car in x:
            vok += 1
        else:
           kos +=1 
    vokal = len(nama)
    return (vokal, vok, kos)

#nomer 4
def rerata(b):
    a=len (b)
    d=0
    for x in range (a):
        d+=b[x]
        c=d/a
    return c

#nomer 5
from math import sqrt as sq
def apakahPrima(n):
    n = int(n) #kalau pecahan, hilangkan pecahannya
    assert n>=0 #hanya menerima bilngan non-negatif
    primaKecil = [2,3,5,7,11] #kalau angkanya kecil, akaan
    bukanPrKecil = [0,1,4,6,8,10] #tertangkap disini
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2, int(sq(n))+1): #cukup sampai akarnya
            if (n % 3) == 0:
                print (n, "bukan bilangan prima")
            else:
                print (n, "angka prima")
        return n 
#nomer 6
a = 2
b = 100
if a >=1 and b>1:
   for x in range (a , b):
         prima = True
         for i in range (2, x):
                if (x%i==0):
                    prima = False
         if prima == True:
                print (x)
else :
    print ("waww")


#nomer 7
def faktorPrima(x):
    a = []

    b = []

    hasil = 0
    bil = x
    prima = True
    for i in range(2, x):
        prima = True
        for u in range (2, i):
            if i % u == 0 :
                prima = False
        if prima :
            a.append(i)

    idx = 0
    while bil > 1:
        try :
            if (bil % a[idx]) == 0:
                hasil = bil/a[idx]
                bil = hasil
                b.append(a[idx])

            else:
                idx = idx + 1
        except IndexError :
            break
    print(b)

#nomer 8
def apakahTerkandung(a,b):
    return a.lower() in b.lower()

#nomer 9
def seto(n):
    result = []
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            result.append("python UMS")
        elif x % 3 == 0:
            result.append("python")
        elif x % 5 == 0 :
            result.append("UMS")
        else :
            result.append(str(x))
    return result
def main():
    print(", ".join(seto(100)))
main()

#nomer 10
from math import sqrt as akar
def selesaikanABC(a, b, c):
    print()
    a= float(a)
    b= float(b)
    c= float(c)
    D= b**2-4*a*c
    if D<0:
        return "determinannya negatif. persamaan tidak mempunyai akar real"
    else:
        x1= (-b+akar(D))/(2*a)
        x2= (-b-akar(D))/(2*a)
        hasil = (x1, x2)
        return hasil

#nomer 11
def tahunKabisat(n):
    if (n % 4 == 0 & n % 100 == 0 & n % 400 ==0):
        return n, "True, Tahun Kabisat"
    else:
        return n, "False, Bukan Tahun Kabisat"

#nomer 12
#from random import randint as r
#a = r(1, 100)
#i = 1
#x = input ("Masukkan Tebakan ke-%i:>" %i)
#while x != a:
#    i += 1
#    if int(x) < a:
 #       print("itu terlalu kecil. Coba Lagi!!")
  #      x = input("Masukkan Tebakan ke-%i:> " %i)
   # else:
    #    print("itu terlalu Besar. Coba Lagi!!")
     #   x = input("Masukkan Tebakan ke-%i:> " %i)
#print("Ya. Anda Benar")


#nomer 13
def formatRupiah(n):
    hasil = ""
    x = 0
    for i in str(n)[::-1]:
        if x < 3:
            hasil += i
            x+=1
        else:
            hasil = hasil +"."+i
            x = 1
    return "Rp. "+ hasil[::-1]
