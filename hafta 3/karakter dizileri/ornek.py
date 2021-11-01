# -*- coding: UTF-8 -*-

liste=[12,312,321,"dsa"]
ad="ahmet"

# 0 indis
l=liste[0]
a=ad[0]
son_eleman=ad[-2] # 3
print(son_eleman)

print(len(ad))

for k in ad:
    print(k)

# dilimlemek slice
# [baslangic:bitis] sonuncu dahil edil 0,1
print(ad[0:2])
print(ad[3:5])

def ilk_son_harf_buyut(kelime):
    ilk=kelime[0].upper()
    if kelime[-1] =="i":
        son="İ"
    else:
        son = kelime[-1].upper()
    
    aralik = kelime[1:-1]
    print(ilk+aralik+son) 

ilk_son_harf_buyut("veli")

bozuk_ifade="slm napiyorsünuz kib"
# replace
ifade=bozuk_ifade.replace("slm","selam")
ifade=ifade.replace("i","ı")
ifade=ifade.replace("ü","u")


print(ifade)

atasozleri=["Akıllı bizi arayıp sormaz deli bacadan akar!",
"Ağa güçlü olunca kul suçlu olur!",
"Avcı ne kadar hile bilirse ayı da o kadar yol bilir!",
"Lafla pilav pişse deniz kadar yağ benden!",
"Zenginin gönlü oluncaya kadar fukaranın canı çıkar!"]

kelime_liste=[]
for k in atasozleri:
    cumle=k.replace("!","")
    cumle = cumle.lower()
    # belirli bir karaktere göre cümleyi bölme
    kelime_liste = kelime_liste+cumle.split(" ")
print(kelime_liste)
"""
# yukarıdaki kelime listesinde her bir kelimenin
# kaç kere geçtiğini hesaplayınız.

tekrar_sozluk = {}
for kelime in kelime_liste:
    if kelime in tekrar_sozluk.keys():
        tekrar_sozluk[kelime] = tekrar_sozluk[kelime] +1
    else:
        tekrar_sozluk[kelime]=1

print(tekrar_sozluk)
"""

# sesli harf sayısını bulunuz.
sesliler = "a,e,u,ü,i,ı,o,ö"
sesli_liste = sesliler.split(",")
print(sesli_liste)
sesli_toplam = 0
for k in kelime_liste:
    for s in sesli_liste:
        if s in k:
            sesli_toplam=sesli_toplam+1

print(sesli_toplam)
