# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 17:16:13 2021

@author: Selcuk
"""

giris = """
(1) topla
(2) cikar
(3) carp
(4) bol
(5) karesini hesapla
(6) kare kök hesapla
"""

print(giris)

soru = input("Yapmak istediğiniz işlemin numarasını girin: ")

secenek1 = "(1) topla"
secenek2 = "(2) cikar"
secenek3 = "(3) carp"
secenek4 = "(4) bol"
secenek5 = "(5) karesini hesapla"
secenek6 = "(6) kare kök hesapla"

print(secenek1, secenek2, secenek3, secenek4, secenek5, secenek6, sep="\n")

if soru == "1":
    sayi1 = int(input("Toplama için ilk sayıyı girin: "))
    sayi2 = int(input("Toplama için ikinci sayıyı girin: "))
    print(sayi1, "+", sayi2, "=", sayi1 + sayi2)

elif soru == "2":
    sayi3 = int(input("Çıkarma işlemi için ilk sayıyı giriniz: "))
    sayi4 = int(input("Çıkarma işlemi için ikinci sayıyı giriniz: "))
    print(sayi3, "-", sayi4, "=", sayi3 - sayi4) 
    
elif soru == "3":
    sayi5 = int(input("Çarpma işlemi için ilk sayıyı giriniz: "))
    sayi6 = int(input("Çarpma işlemi için ikinci sayıyı giriniz: "))
    print(sayi5, "*", sayi6, "=", sayi5 * sayi6)
    
elif soru == "4":
    sayi7 = int(input("Bölme ilemi için ilk sayıyı giriniz: "))
    sayi8 = int(input("Bölme işlemi için ikinci sayıyı giriniz: "))
    print(sayi7, "/", sayi8, "=", sayi7 / sayi8)
    
elif soru == "5":
    sayi9 = int(input("Hangi sayının karesini öğrenmek istiyorsunuz: "))
    print(sayi9, "Sayının karesi: ", sayi9 ** 2)
    
elif soru == "6":
    sayi10 = int(input("Karekök değerini öğrenmek istediğiniz sayıyı giriniz: "))
    print(sayi10, "Bu sayının karekök değeri: ", sayi10 ** 0.5)
    
else:
    print("Yanlış değer girdiniz.")
    print("Aşağıdaki seçeneklerden birtanesini seçiniz: ", giris)







