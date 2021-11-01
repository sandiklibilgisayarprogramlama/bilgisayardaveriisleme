# düzenli ifadeler
# regular expression
# stop words u,you, 

import re

# match
# search
cumle = "merhaba bu derste duzenli ifadeleri konusacagiz, ders bitimi saat 14:00 olacak."
aranacak = "ders"
"""
kelimeler = cumle.split(" ")
for ke in kelimeler:
    if ke == aranacak:
        print("bulundu")
        break
"""
# match -> cumlenin basına bakar aranacak kelime yoksa
# none dondurur
"""
if re.match(aranacak,cumle) is not None:
    print("bulundu")
else:
    print("bulunamadı")
"""
# search -> sadece ilk bulunan metni saptar
#sonuc=re.search(aranacak,cumle)
#print(cumle[0:sonuc.span()[0]]+cumle[sonuc.span()[1]:])

#findall hepsini getirir.
print(re.findall(aranacak,cumle))

liste = ["özcan", "mehmet", "süleyman", "selim",
"kemal", "özkan", "esra", "dündar", "esin",
"esma", "özhan", "özlem"]

print(re.findall("para[ımızlar]"
,"bizim bir sürü dolarımız var,sen dolarr ne bilir misin ?"))
"""
izin_verilen_karakterler = "rımız"
#["r","ı","m","ı","z"]

aranacak = "dolar"
cumle= "bizim bir sürü dolarımız var,sen dolarr ne bilir misin ?"
cumle = cumle.replace(","," ")
for kelime in cumle.split(" "):
    if aranacak in kelime:
        for k in list(izin_verilen_karakterler):
            if k in kelime:
                print("bulundu",kelime)
                break
"""

# [0-9] aranacak metinde rakam olup olmadığını bulur
# \ escape işareti
print(re.findall("\$[0-9]","this box is $10"))

# [A-Z] aranacak metin içinde büyük harf var mı bulur.
print(re.findall("[A-Z]","selam naber ahmet"))
# [a-z] aranacak metinde büyük harf var mı kontrolü
print(re.findall(".[aeuü].","merhaba a9a a8v"))
# arasında a,e,u,ü olanları getirdik.
"""
bir cümledeki üçüncü ve dördüncü karakterleri sesli harf olan kelimeleri
bulunuz.
..[aeıioöuüAEIİOÖUÜ][aeıioöuüAEIİOÖUÜ].

değişken tanımlama kurallarına göre çalışan ve yanlış tanımlamaları
saptayan düzenli ifade kodu
"""

print(re.findall("[A-Za-z_][A-Za-z_0-9]*","9say1 sa8!ı Sa6mc da9__ "))

# kendinden önce gelen ifadenin sıfırdan fazla en az bir kez tekrar etmesini
# istediğimiz durumlarda kullanılır.

print(re.findall("[A-Z]+","Merhaba MErhaba merhaba"))


