# This is a sample Python script.
from OrtancaSayi import Ortanca
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# sayilar = []
#
# def sayi_giris(sayi):
#     j = 1
#     while sayi:
#         sayilar.append(input("ekrana " + str(j) + ". sayıyı girin: "))
#         sayi = sayi - 1
#         j = j + 1
#
# def bul_ortanca():
#     medium = 0
#     if sayilar[0] < sayilar[1]:
#         if sayilar[1] < sayilar[2]:
#             medium = sayilar[1]
#         elif sayilar[0] < sayilar[2]:
#             medium = sayilar[2]
#         else:
#             medium = sayilar[0]
#     else:
#         if sayilar[0] < sayilar[2]:
#             medium = sayilar[0]
#         elif sayilar[1] < sayilar[2]:
#             medium = sayilar[2]
#         else:
#             medium = sayilar[1]
#     print("ortanca sayı = " + medium)
#


def main ():
    print("uygulama başlıyor.")

    #burada yenı class oluşturulacak
    a = 1
    while a:
        #class metotları çağırılacak
        ortObj = Ortanca()
        ortObj.sayi_giris(3)
        print(ortObj.sayilar)
        ortObj.bul_ortanca()
        a = input("Devam etmek ıster mısınız? 0:H ")
        #sayilar.clear()

    print("uygulama sonlandı.")
main()