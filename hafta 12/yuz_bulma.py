import cv2
import sys
fotograf = cv2.imread("maskeli.jpg")
gray = cv2.cvtColor(fotograf, cv2.COLOR_BGR2GRAY)
yuz_belirleme = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
yuz = yuz_belirleme.detectMultiScale(
   gray,
   scaleFactor=1.075,
   minNeighbors=5,
   minSize=(15, 15))

for (x, y, w, h) in yuz:
   cv2.rectangle(
   fotograf,
   (x, y),
   (x + w, y + h),
   (0,0,255),
   2)
durum = cv2.imwrite("fotobulma.jpg", fotograf)
print("[ Bilgi Mesajı… ] Görsel kaydedildi: ", durum)
