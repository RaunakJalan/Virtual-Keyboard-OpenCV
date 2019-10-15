import cv2
import numpy as np
from pynput.mouse import Button, Controller
import tkinter as tk

mouse=Controller()

#basically window size
root = tk.Tk()
sx = root.winfo_screenwidth()
sy = root.winfo_screenheight()

#capture resolution
(camx,camy)=(320,240) #as we are defining this we dont have to resize the img
                    #

#color range(this is of yellow color)
lowerBound=np.array([20, 80, 100])
upperBound=np.array([40,200,300])

cam= cv2.VideoCapture(0)


kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))


while True:
    ret, img=cam.read()
    #img=cv2.resize(img,(340,220)) no need of this kyunki capture resol. mention kar chuke hain

    #convert BGR to HSV
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # create the Mask
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
    #morphology
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal=maskClose
    conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    if(len(conts)==1):

        x,y,w,h=cv2.boundingRect(conts[0])
        # rectangle around colored finger
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        #centroid(int)
        cx=x+w//2
        cy=y+h//2
        
        #circle in the midpoint of colored finger
        cv2.circle(img, (cx,cy),2,(0,0,255),2)

       #converting image res coordinate to screen(x aur y coordinate ko camera se pura screen pe kar dega)
        mouseLoc=(cx*sx//camx,cy*sy//camy)

        while mouseLoc!=(cx*sx//camx,cy*sy//camy):
            pass

        mouse.press(Button.left)
    cv2.rotate(img,rotateCode=cv2.ROTATE_180)    
    cv2.imshow("cam",img)
    cv2.waitKey(5)
        
