class Ortanca:

    def __init__(self):
        print("ortanca classında nesne oluşturuldu")
        self.sayilar = []

    def sayi_giris(self, sayi):
        j = 1
        while sayi:
            self.sayilar.append(input("ekrana " + str(j) + ". sayıyı girin: "))
            sayi = sayi - 1
            j = j + 1

    def bul_ortanca(self):
        medium = 0
        if self.sayilar[0] < self.sayilar[1]:
            if self.sayilar[1] < self.sayilar[2]:
                medium = self.sayilar[1]
            elif self.sayilar[0] < self.sayilar[2]:
                medium = self.sayilar[2]
            else:
                medium = self.sayilar[0]
        else:
            if self.sayilar[0] < self.sayilar[2]:
                medium = self.sayilar[0]
            elif self.sayilar[1] < self.sayilar[2]:
                medium = self.sayilar[2]
            else:
                medium = self.sayilar[1]
        print("ortanca sayı = " + medium)

