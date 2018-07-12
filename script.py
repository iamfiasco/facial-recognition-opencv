import cv2
import sys
color = cv2.imread(sys.argv[1],1)
bw = cv2.cvtColor(color,cv2.COLOR_BGR2GRAY)
classf = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
faces=classf.detectMultiScale(bw,1.1,5)
for (x,y,w,h) in faces:
	cv2.rectangle(color,(x,y),(x+w,y+h),(0,0,255),5)
cv2.imwrite("output.jpg",color)

