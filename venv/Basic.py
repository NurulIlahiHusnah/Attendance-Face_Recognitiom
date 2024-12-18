import cv2
import numpy as np 
import face_recognition

imgJeff = face_recognition.load_image_file('ImageBasic\Jeff Bezos.jpg')
imgJeff = cv2.cvtColor(imgJeff, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImageBasic\Mark Zuckerberg.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgJeff)[0]
encodeJeff = face_recognition.face_encodings(imgJeff)[0]
cv2.rectangle(imgJeff,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

faceTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceTest[3],faceTest[0]),(faceTest[1],faceTest[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodeJeff],encodeTest)
faceDis = face_recognition.face_distance([encodeJeff],encodeTest)
print(results, faceDis)
cv2.putText(imgTest,f'{results} {faceDis[0],2}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


cv2.imshow('Jeff Bezos', imgJeff)
cv2.imshow('Mark Zuckerberg test',imgTest)
cv2.waitKey(0)