#SORU1:
print("VÜCUT KİTLE İNDEKSİ HESAPLAMA")
boy=float(input("Lütfen boyunuzu giriniz:(m) "))
kilo=int(input("Lütfen kilonuzu giriniz: (kg)"))

indeks=kilo/(boy*boy)

indeks=f"vücut kitle indeksiniz {indeks}"
print(indeks)


#SORU2:

maas = int(input("Lütfen Maaşı Giriniz"))
zamOrani = int (input("Zam Oranını Giriniz"))
zamliMaas = (maas*zamOrani/100)+ (maas)
print (zamliMaas)

#SORU3:
sayi1=int(input("Birinci sayıyı girin:"))
sayi2=int(input("ikinci sayıyı girin:"))
sayi3=int(input("Üçüncü sayıyı girin:"))

if (sayi1 >= sayi2) and (sayi1 >= sayi3):
   enBuyukSayı = sayi1
elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
   enBuyukSayı = sayi2
else:
   enBuyukSayı = sayi3
 
print("En büyük sayı: ", enBuyukSayı)


#SORU4:
r=int(input("Yarı Çapı Girin: "))
cevre=2*3.14*r
alan=3.14*r*r
print("Çevre: ",cevre)
print("Alan: ",alan)

#SORU5:
sayi1=input("sayı giriniz: ")
ters=sayi1[::-1]
if sayi1==ters:
    print("girdiğin sayı polindrom bir sayıdır")
else:
    print("bu sayı polindrom değil")