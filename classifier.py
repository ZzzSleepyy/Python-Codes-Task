import cv2 as cv
from cvzone.ClassificationModule import Classifier

mydat = Classifier("test/keras_model.h5", "test/labels.txt")

capture = cv.VideoCapture(0)

while True:
    e,img = capture.read()
    
    pred, index = mydat.getPrediction(img,scale=1,color=(0,0,0))
    
    print(pred,index)
    cv.imshow("AI", img)
    
    key = cv.waitKey(1)
    
    if key == 27:
        break
    
capture.release()
