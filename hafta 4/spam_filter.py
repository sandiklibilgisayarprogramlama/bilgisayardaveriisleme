from util import load_dataset

spam_words = ["free","txt","mobile","stop","text","prize","won"]
ham_words = ["dont","ill","got","like","know","come","love","good"]

satir_liste = load_dataset("SMSSpamCollection")

ham_sayi = 0
spam_sayi= 0
spam_bulanan = 0
ham_bulunan = 0
for satir in satir_liste:
    bolunmus_satir=satir.split("\t")
    if bolunmus_satir[0] == "spam":
        spam_sayi = spam_sayi+1
        mesaj = bolunmus_satir[1]
        mesaj = mesaj.lower()
        for spam_w in spam_words:
            if spam_w in mesaj:
                spam_bulanan=spam_bulanan+1
                break
    else:
        ham_sayi=ham_sayi+1
        mesaj = bolunmus_satir[1]
        mesaj = mesaj.lower()
        for ham_w in ham_words:
            if ham_w in mesaj:
                ham_bulunan=ham_bulunan+1
                break
    

print("ham\thambulunan\tspam\tspambulunan")
print(str(ham_sayi)+"\t"+str(ham_bulunan)+"\t"+str(spam_sayi)+"\t"+str(spam_bulanan))

"""
ham ve spam mesajlardaki noktalama işareti sayısını bulunuz
spam_filtera ekleyerek sonucu nasıl etkilediğini görünüz.
saat kontrolü
para birimi
"""