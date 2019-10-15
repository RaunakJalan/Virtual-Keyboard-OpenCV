#required libraries

import cv2
import numpy as np
import pyautogui
from tkinter import messagebox
import tkinter as tk

pyautogui.FAILSAFE = False

#root window of tkinter
root = tk.Tk()

#range of desired color(yellow)
lowerBound=np.array([20, 80, 100])
upperBound=np.array([40,200,300])
hd = cv2.CascadeClassifier(r'hand.xml')

#size of kernel(morphology is performed on this size of kernel)
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))


cap = cv2.VideoCapture(0)


#capture resolution
cap.set(3,1366)
cap.set(4,768)

if cap.isOpened():
    ret,keyboard = cap.read()
else:
    ret = False

#function to define the letter keys in the upper part of keyboard(their width,height and thickness) as well as its fonts
    
def letter(x,y,text):

        #KEYS:

        width = 80
        height = 80

        if text == "enter" or text == "shift":
            width = 140
            
        th = 2 #thickness
        cv2.rectangle(keyboard,(x+th,y+th),(x+width-th,y+height-th),(0,0,255),th)
        #cv2.rectangle(keyboard,(110,0),(210,100),(255,0,0),3)


        #Text Settings:(fonts and size)

        font_letter = cv2.FONT_HERSHEY_PLAIN
        font_scale = 4
        font_th = 3
        if text == "enter" or text == "shift":
            font_scale = 3
            font_th = 2
        #to get height and width of the particular letter
        text_size = cv2.getTextSize(text,font_letter,font_scale,font_th)[0]
        #storing height and width
        width_text, height_text = text_size[0],text_size[1]
        #to align the letter in the middle of the key
        text_x = int((width - width_text) / 2) + x
        text_y = int((height + height_text) / 2) + y
        
        cv2.putText(keyboard, text, (text_x,text_y),font_letter,font_scale,(0,0,255),font_th)

#function to define the number keys in the lower part of keyboard(their width,height and thickness) as well as its fonts
def numbers_draw(x,y,text):

        #KEYS:

        width = 80
        height = 80

        if text == "enter" or text == "shift":
            width = 140
            
        th = 2 #thickness
        cv2.rectangle(keyboard,(x+th,y+th),(x+width-th,y+height-th),(0,0,255),th)
        #cv2.rectangle(keyboard,(110,0),(210,100),(255,0,0),3)


        #Text Settings:

        font_letter = cv2.FONT_HERSHEY_PLAIN
        font_scale = 4
        font_th = 3
        if text == "enter" or text == "shift":
            font_scale = 3
            font_th = 2
         #to get height and width of the particular number
        text_size = cv2.getTextSize(text,font_letter,font_scale,font_th)[0]
        #storing height and width
        width_text, height_text = text_size[0],text_size[1]
        #to align the number in the middle of the key
        text_x = int((width - width_text) / 2) + x
        text_y = int((height + height_text) / 2) + y
        
        cv2.putText(keyboard, text, (text_x,text_y),font_letter,font_scale,(0,0,255),font_th)
'''
 ______ ______
|      |      |
|      |      |
|______|______|
|      |      |
|      |      |
|______|______|
'''
    
def click_keys(cent_x,cent_y,x,y,w,h,coords):
    pos_key = []
    count_let = 0
    row_no = 0
    clicked = False
    r_index,c_index = -1,-1
    for row in range(0,len(coords)):
        col_no = 0
        for col in range(0,len(coords[row])):
            #print(row,col)
            if cent_x > coords[row][col][0] and cent_x < coords[row][col][0]+80:
                if cent_y>coords[row][col][1] and cent_y < coords[row][col][1]+80:
                    clicked = True
                    r_index,c_index = row,col
                    break
            count_let+=1
            
        if clicked == True:
            break
    if r_index == -1 and c_index == -1:
        return coords[0][0], r_index,c_index
    else:
        return coords[r_index][c_index],r_index,c_index
        
def key_light(x,y,text):
    width = 80
    height = 80
        
    if text == "enter" or text == "shift":
        width = 140
            
    th = 2 #thickness
    cv2.rectangle(keyboard,(x+th,y+th),(x+width-th,y+height-th),(255,255,255),-1)
        #cv2.rectangle(keyboard,(110,0),(210,100),(255,0,0),3)


text_cli = ''
ind_key=[]
frame_no = 1
coords_mus = []
frame_no_mus = 1
playing = False
clicked_mus = False
while True:

    ret,keyboard = cap.read()

    #flipping the camera so as to get image in same direction as of camera
    keyboard = cv2.flip(keyboard,1)

    gray_hand = cv2.cvtColor(keyboard,cv2.COLOR_BGR2GRAY)
    hand = hd.detectMultiScale(gray_hand)
    
    #sequence of letters in keyboard
    alphabet_letter = "q w e r t y u i o p [ ] \ a s d f g h j k l ; ' enter z x c v b n m , . @ shift".split()
    x_coords = []
    y_coords = []
    coords = []
    c = 0
    #max_lim = 1500
    x_add = 0 # extra length of particular keys(i.e;shift and enter)
    line=0
    for i in range(0,768,90):  #(height(column) of screen is 768 and 80 is the width of key .90 is taken bcz we included space in between) y-axis
        #appennding value of y-axis 
        coords.append([])
        for j in range(0,1366,95): #similar for x axis
            if(c!=36):
                if j+80+x_add < 1366:
                    letter(j+x_add,i,alphabet_letter[c])
                    x_coords.append(j+x_add)
                    y_coords.append(i)
                    coords[line].append([j+x_add,i])
                    if alphabet_letter[c] == "enter" or alphabet_letter[c] == "shift":
                        x_add = 80
                        
                    if alphabet_letter[c] == "\\" or alphabet_letter[c] == "enter" or alphabet_letter[c] == "shift":
                        break
                    c+=1
                else:
                    pass
            else:
                break

        c+=1
        line+=1
        if c == 36:
            break


    num_side = '* - + % / 5 6 7 8 9 0 1 2 3 4'.split()
    num = '1 2 3 4 5 6 7 8 9 0'.split()

    total = []

    c = 0

    for i in alphabet_letter:
        total.append(i)
    for i in num_side:
        total.append(i)

        
    #  12 key in first row(letters)
    fin_tot = [total[0:13]]
    fin_tot.append(total[13:25])
    fin_tot.append(total[25:36])
    # 5 key(numbers)
    fin_tot.append(total[36:41])
    fin_tot.append(total[41:46])
    fin_tot.append(total[46:51])


    start_num_x = 0
    start_num_y = y_coords[-1]+150
    c = 0
    count = 1

    for y_num in range(start_num_y,768, 90):
        count = 1
        coords.append([])
        for x_num in range(0,1366,85):
            if(c!=15):
                if count <= 5:
                    numbers_draw(x_num,y_num,num_side[c])
                    x_coords.append(x_num+x_add)
                    y_coords.append(y_num)
                    coords[line].append([x_num,y_num])
                    count+=1
                    c+=1
                else:
                    break
            else:
                break
        line+=1
        if c == 15:
            break

    cv2.putText(keyboard, "Slide finger for sliding operations", (x_num+100,start_num_y-30),cv2.FONT_HERSHEY_PLAIN,2,(0,120,255),2)
    cv2.rectangle(keyboard, (x_num+20,start_num_y-10),(x_num+300+550,start_num_y-105+450),(0,255,0),3)
    #converting img to HSV
    imgHSV= cv2.cvtColor(keyboard,cv2.COLOR_BGR2HSV)
    # create the Mask(as per your color selection)
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
    #morphology open(erosion followed by dilation)
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    #morphology close(dilation followed by erosion )
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal=maskClose

    x1=445
    y1=320
    x2=1275
    y2=675
    
    # finding contours
    conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    # condition for closed contours
    if(len(conts)==1):

        x,y,w,h=cv2.boundingRect(conts[0])
        

        if x>x1 and x+w<x2 and y>y1 and y+h<y2: 
            cv2.rectangle(keyboard,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.rectangle(keyboard,(445,320),(1275,675),(255,0,255),2)
            #centroid of finger(taken in int)
            cx=x+w//2
            cy=y+h//2
            
            cv2.circle(keyboard, (cx,cy),2,(0,0,255),2)
            #moving cursor position
            pyautogui.moveTo(x,y)
            #if  frame is 1 then take coordinate as w*h
            if frame_no_mus == 1:
                coords_mus.append(w*h)
            #if  frame is 5 then take coordinate as w*h
            if frame_no_mus == 5:
                coords_mus.append(w*h)
                frame_no_mus = 0
                #diff of coords between the frame(controlling music using hand gesture)
                if coords_mus[1]-coords_mus[0]>500:
                    clicked_mus = True
                    pyautogui.click(clicks = 2,interval = 0.25)
                    playing = True

                    
                coords_mus = []
                
            
            frame_no_mus+=1
                

        else:
            
    
            cx=x+w//2
            cy=y+h//2
            
            #circle in the midpoint of colored finger
            cv2.circle(keyboard, (cx,cy),2,(255,255,255),2)
            # rectangle around colored finger(adjustment of size is done[hit and trial])
            if x+w<x+50 and y+h< y+50:
                cv2.rectangle(keyboard,(x,y),(x+w,y+h),(255,255,255),2)
            else:
                cv2.rectangle(keyboard,(x,y),(x+50,y+50),(255,255,255),2)

        
        #clicking of keys by comparing frame
        
        if frame_no == 1:
            ind_key1,r_ind1,c_ind1 = click_keys(cx,cy,x,y,w,h,coords)
        if frame_no == 12:
            ind_key4,r_ind4,c_ind4 = click_keys(cx,cy,x,y,w,h,coords)
            frame_no = 0
            if r_ind1 != -1 and c_ind1 != -1:
                if len(ind_key1) != 0:
                    if ind_key1 == ind_key4 and r_ind1 == r_ind4 and c_ind1 == c_ind4:
                        key_cli = fin_tot[r_ind1][c_ind1]
                        key_light(ind_key1[0],ind_key1[1],key_cli)
                        pyautogui.press(key_cli)
                        text_cli+=key_cli
                        
                '''
                if fin_tot[r_ind][c_ind] == "enter":
            
                    text_cli += '\n'
                else:
                '''
        frame_no += 1

    for (q,r,t,b) in hand:
        if q>x1 and q+t<x2 and r>y1 and r+b<y2 and t*b>9000:
            cv2.rectangle(keyboard,(q,r),(q+t,r+b),(255,255,255),2)
            if clicked_mus == True:
                if q < 500 and playing==True:
                    pyautogui.press(' ')
                    playing = False 
                elif q+t > 1000 and playing == False:
                    pyautogui.press(' ')
                    playing = True


        
            
        #print(text_cli)
                  
    cv2.imshow("Keyboard",keyboard)

    if cv2.waitKey(2) == 13:
        messagebox.showinfo( "Created By:","Ankit Singh\nKanchan Kumari\nRaunak Jalan")
        #destroying the tkinter window
        root.destroy()
        break

root.mainloop()
cap.release()
cv2.destroyAllWindows()
