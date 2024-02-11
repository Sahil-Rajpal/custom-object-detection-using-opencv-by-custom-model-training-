# this can be done by using two ways : 1st is by downloading the images and then feed to the model
                                    # 2nd is the done by taking feed from the webcam directly and simulatneously saving the photos and
                                        #  converting it into a single file "xml file"

import cv2
import os
import time

###################################################

mypath="C:/Users/sahil/Desktop/img"

camerano=2
camerabrightness =190
moduleval=10 # save every ith frame to avoid repetition
minblr= 500 # smaller value means more bluriness present
grayimg= False # image saved colored or gray
savedata=True # save data flag
showimage=True # image display flag
imgwidth=180
imgheight=120

###############################################

global countFolder
cap=cv2.VideoCapture(camerano)
cap.set(3,640)
cap.set(4,480)
cap.set(10,camerabrightness)

count=0
countsave=0
def saveDataFunc():
    global countFolder
    countFolder=0
    while os.path.exists((mypath+str(countFolder))):
        countFolder=countFolder+1
    os.makedirs(mypath+str(countFolder))

if savedata:saveDataFunc()

while True:
    success , img= cap.read()
    img=cv2.resize(img,(imgwidth,imgheight))
    if grayimg:img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    if savedata:
        blur=cv2.Laplacian(img,cv2.CV_64F).var()
        if count % moduleval == 0 and blur > minblr:
            nowTime=time.time()
            cv2.imwrite(mypath+str(countFolder))
            '/'+str(countsave)+" "+ str(int(blur))+" "+str(nowTime)+".png",img
            countsave+=1
        count+=1
    if showimage:
        cv2.imshow("image",img)
    if cv2.waitKey((1)) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

        

