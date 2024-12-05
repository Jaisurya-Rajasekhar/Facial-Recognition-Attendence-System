import cv2
import numpy as np
import face_recognition

# Load and convert images
imgElon = face_recognition.load_image_file('ImagesBasics/elonmusk1.jpeg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('ImagesBasics/Elon musk2.jpeg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)  #to convert the image into rgb

faceLoc=face_recognition.face_locations(imgElon)[0]
encodeElon=face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)


faceLocTest=face_recognition.face_locations(imgTest)[0]
encodeTest=face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)


results=face_recognition.compare_faces([encodeElon],encodeTest)
faceDis=face_recognition.face_distance([encodeElon],encodeTest)
print(results, faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)



# Display images with different window names
cv2.imshow('Elon Musk Image 1', imgElon)
cv2.imshow('Elon Musk Image 2', imgTest)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()