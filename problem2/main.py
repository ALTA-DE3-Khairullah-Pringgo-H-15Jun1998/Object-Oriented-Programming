class Volume:
    def __init__(self, a, b, c, d, e, f):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.d = int(d)
        self.e = int(e)
        self.f = int(f)

    def hitung_volume_kubus(self):
        import math
        return pow(self.a,3)

    def hitung_volume_balok(self):
        return self.b * self.c * self.d
    
    def hitung_volume_tabung(self):
        return int((22 * self.e * self.e * self.f)/7)
    
a = int(input("Masukkan sisi kubus: "))
b = int(input("Masukkan panjang balok: "))
c = int(input("Masukkan lebar balok: "))
d = int(input("Masukkan tinggi balok: "))
e = int(input("Masukkan jari-jari tabung: "))
f = int(input("Masukkan tinggi tabung: "))
kubus = Volume(a, b, c, d, e, f)
balok = Volume(a, b, c, d, e ,f)
tabung = Volume(a, b, c, d, e, f)
print("Volume Kubus:", kubus.hitung_volume_kubus())
print("Volume Balok: ", balok.hitung_volume_balok())
print("Volume Tabung:", tabung.hitung_volume_tabung())
