from util import load_dataset
stop_words = ['those', 'on', 'own', '’ve', 'yourselves', 'around', 'between', 'four', 'been', 'alone', 'off', 'am', 'then', 'other', 'can', 'regarding', 'hereafter', 'front', 'too', 'used', 'wherein', '\'ll', 'doing', 'everything', 'up', 'onto', 'never', 'either', 'how', 'before', 'anyway', 'since', 'through', 'amount', 'now', 'he', 'was', 'have', 'into', 'because', 'not', 'therefore', 'they', 'n’t', 'even', 'whom', 'it', 'see', 'somewhere', 'thereupon', 'nothing', 'whereas', 'much', 'whenever', 'seem', 'until', 'whereby', 'at', 'also', 'some', 'last', 'than', 'get', 'already', 'our', 'once', 'will', 'noone', "'m", 'that', 'what', 'thus', 'no', 'myself', 'out', 'next', 'whatever', 'although', 'though', 'which', 'would', 'therein', 'nor', 'somehow', 'whereupon', 'besides', 'whoever', 'ourselves', 'few', 'did', 'without', 'third', 'anything', 'twelve', 'against', 'while', 'twenty', 'if', 'however', 'herself', 'when', 'may', 'ours', 'six', 'done', 'seems', 'else', 'call', 'perhaps', 'had', 'nevertheless', 'where', 'otherwise', 'still', 'within', 'its', 'for', 'together', 'elsewhere', 'throughout', 'of', 'others', 'show', '’s', 'anywhere', 'anyhow', 'as', 'are', 'the', 'hence', 'something', 'hereby', 'nowhere', 'latterly', 'say', 'does', 'neither', 'his', 'go', 'forty', 'put', 'their', 'by', 'namely', 'could', 'five', 'unless', 'itself', 'is', 'nine', 'whereafter', 'down', 'bottom', 'thereby', 'such', 'both', 'she', 'become', 'whole', 'who', 'yourself', 'every', 'thru', 'except', 'very', 'several', 'among', 'being', 'be', 'mine', 'further', 'n\'t', 'here', 'during', 'why', 'with', 'just', "'s", 'becomes', '’ll', 'about', 'a', 'using', 'seeming', "'d", "'ll", "'re", 'due', 'wherever', 'beforehand', 'fifty', 'becoming', 'might', 'amongst', 'my', 'empty', 'thence', 'thereafter', 'almost', 'least', 'someone', 'often', 'from', 'keep', 'him', 'or', '\'m', 'top', 'her', 'nobody', 'sometime', 'across', '\'s', '’re', 'hundred', 'only', 'via', 'name', 'eight', 'three', 'back', 'to', 'all', 'became', 'move', 'me', 'we', 'formerly', 'so', 'i', 'whence', 'under', 'always', 'himself', 'in', 'herein', 'more', 'after', 'themselves', 'you', 'above', 'sixty', 'them', 'your', 'made', 'indeed', 'most', 'everywhere', 'fifteen', 'but', 'must', 'along', 'beside', 'hers', 'side', 'former', 'anyone', 'full', 'has', 'yours', 'whose', 'behind', 'please', 'ten', 'seemed', 'sometimes', 'should', 'over', 'take', 'each', 'same', 'rather', 'really', 'latter', 'and', 'ca', 'hereupon', 'part', 'per', 'eleven', 'ever', '\'re', 'enough', "n't", 'again', '\'d', 'us', 'yet', 'moreover', 'mostly', 'one', 'meanwhile', 'whither', 'there', 'toward', '’m', "'ve", '’d', 'give', 'do', 'an', 'quite', 'these', 'everyone', 'towards', 'this', 'cannot', 'afterwards', 'beyond', 'make', 'were', 'whether', 'well', 'another', 'below', 'first', 'upon', 'any', 'none', 'many', 'serious', 'various', 're', 'two', 'less', '\'ve']

satir_liste = load_dataset("SMSSpamCollection")

sozluk = {}
for satir in satir_liste:
    # ham   Ok lar... Joking wif u oni...
    bolunmus_satir=satir.split("\t")
    if bolunmus_satir[0]=="ham":
        mesaj = bolunmus_satir[1]
        mesaj = mesaj.replace(".","")
        mesaj = mesaj.replace("!","")
        mesaj = mesaj.replace("?","")
        mesaj = mesaj.replace(";","")
        mesaj = mesaj.replace(":","")
        mesaj = mesaj.replace("\"","")
        mesaj = mesaj.replace(")"," ")
        mesaj = mesaj.replace("("," ")
        mesaj = mesaj.replace("'","")
        mesaj = mesaj.replace("*","")
        mesaj = mesaj.replace("\n","")
        mesaj = mesaj.replace("<","")
        mesaj = mesaj.replace(">","")
        mesaj = mesaj.replace("+","")
        mesaj = mesaj.replace("-","")
        mesaj = mesaj.replace("&","")
        for k in range(0,10):
            mesaj = mesaj.replace(str(k),"")

        mesaj = mesaj.lower()
        # regular expressions
        mesaj_kelimeler = mesaj.split(" ")
        for kelime in mesaj_kelimeler:
            if len(kelime)>2 and kelime not in stop_words:
                if kelime in sozluk.keys():
                    sozluk[kelime] = sozluk[kelime]+1
                else:
                    sozluk[kelime]=1
        
print({k: v for k, v in sorted(sozluk.items(), 
key=lambda item: item[1])})


#spam_words = ["free","txt","mobile","stop","text","prize","won"]
#ham_words = ["dont","ill","got","like","know","come","love","good"]