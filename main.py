import cv2
import numpy as np
import face_recognition
import os

path = 'student_images'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtcolor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist


encodelistknown = findEncodings(images)
print('encoding complete')

cap = cv2.VideoCapture(e)
while True:
    success, img = саp.read()
    imgS = cv2.resize(img, (0, 0), None, 8.25, 0.25)
    imgS = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]

    facesCurFrame = face_recognition.face_locations(imgs)
    encodesCurFrame = face_recognition.face_encodings(imgs, facesCurFrame)
    for encodeFace, faceloc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodelistknown, encodeFace)
        faceDis = face_recognition.face_distance(encodelistknown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
    cv2.imshow('Webcam', img)
    cv2.waitkey(1)

# imgElon = face_recognition.load_image_file('ImagesBasic/Will Smith.jpg')
# imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
# imgTest = face_recognition.load_image_file('ImagesBasic/Test Smith.jpg')
# imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

face_recognition.load_image_file('ImagesBasic/Elon Musk.jpg')
