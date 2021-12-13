import cv2

# resim yükleme
resim = cv2.imread("resimler/ornek.png",cv2.IMREAD_GRAYSCALE)
# cv2.IMREAD_UNCHANGED
"""
cv2.imread("resim yolu", yükleme_tipi)

yükleme_tipi bos bırakılırsa orada cv2.IMREAD_COLOR yazıldığını
kabul eder.
rgb
rgba
"""
print(resim.shape)
# resmin boyutunu gösterir.
# yükseklik,genişlik,kanal (200,200,3)

print(resim[100][100])
# 100x100 üncü piksel değerini gösterir.
resim[100][100]=0
# resim gösterme
cv2.imshow("Örnek Resim",resim)
cv2.waitKey(0)

"""
herhangi bir grayscale resimde piksel değer 0 olan piksellerin
degerini 255 yapan programı yazınız ve sonunda resmi gösteriniz.
"""

