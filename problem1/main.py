# tulis solusi code disini
class LuasKeliling:
    def __init__(self, a, b, c, d, e, f):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.d = int(d)
        self.e = int(e)
        self.f = int(f)

    def hitung_luas_persegi(self):
        return self.a ** 2

    def hitung_luas_segitiga(self):
        return int((self.b*self.c)/2)
    
    def hitung_luas_persegi_panjang(self):
        return self.e * self.f
    
    def hitung_keliling_persegi(self):
        return self.a * 4
    
    def hitung_keliling_segitiga(self):
        return self.b + self.c + self.d
    
    def hitung_keliling_persegi_panjang(self):
        return (2*self.e) + (2*self.f)

a = int(input("Masukkan sisi persegi: "))
b = int(input("Masukkan alas segitiga: "))
c = int(input("Masukkan tinggi segitiga: "))
import math
d = int(math.sqrt(pow(b, 2)+pow(c, 2)))
e = int(input("Masukkan panjang persegi panjang: "))
f = int(input("Masukkan lebar persegi panjang: "))
persegi = LuasKeliling(a, b, c, d, e, f)
segitiga = LuasKeliling(a, b, c, d, e ,f)
persegi_panjang= LuasKeliling(a, b, c, d, e, f)
print("Luas Persegi:", persegi.hitung_luas_persegi())
print("Luas Segitiga: ", segitiga.hitung_luas_segitiga())
print("Luas Persegi Panjang:", persegi_panjang.hitung_luas_persegi_panjang())
print("Keliling Persegi:",persegi.hitung_keliling_persegi())
print("Keliling Segitiga:",persegi.hitung_keliling_segitiga())
print("Keliling Persegi Panjang:",persegi.hitung_keliling_persegi_panjang())