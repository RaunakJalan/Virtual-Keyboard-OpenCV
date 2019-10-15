import cv2
import numpy as np
from pynput.mouse import Button, Controller

mouse=Controller()
#basically window size


lowerBound=np.array([20, 80, 100])
upperBound=np.array([40,200,300])

kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

cap = cv2.VideoCapture(0)



cap.set(3,1366)
cap.set(4,768)

if cap.isOpened():
    ret,keyboard = cap.read()
else:
    ret = False


def letter(x,y,text):

        #KEYS:

        width = 80
        height = 80

        if text == "enter" or text == "shift":
            width = 140
            
        th = 2 #thickness
        cv2.rectangle(keyboard,(x+th,y+th),(x+width-th,y+height-th),(255,0,0),th)
        #cv2.rectangle(keyboard,(110,0),(210,100),(255,0,0),3)


        #Text Settings:

        font_letter = cv2.FONT_HERSHEY_PLAIN
        font_scale = 4
        font_th = 3
        if text == "enter" or text == "shift":
            font_scale = 3
            font_th = 2    
        text_size = cv2.getTextSize(text,font_letter,font_scale,font_th)[0]
        width_text, height_text = text_size[0],text_size[1]
        text_x = int((width - width_text) / 2) + x
        text_y = int((height + height_text) / 2) + y
        cv2.putText(keyboard, text, (text_x,text_y),font_letter,font_scale,(255,0,0),font_th)


def numbers_draw(x,y,text):

        #KEYS:

        width = 80
        height = 80

        if text == "enter" or text == "shift":
            width = 140
            
        th = 2 #thickness
        cv2.rectangle(keyboard,(x+th,y+th),(x+width-th,y+height-th),(255,0,0),th)
        #cv2.rectangle(keyboard,(110,0),(210,100),(255,0,0),3)


        #Text Settings:

        font_letter = cv2.FONT_HERSHEY_PLAIN
        font_scale = 4
        font_th = 3
        if text == "enter" or text == "shift":
            font_scale = 3
            font_th = 2    
        text_size = cv2.getTextSize(text,font_letter,font_scale,font_th)[0]
        width_text, height_text = text_size[0],text_size[1]
        text_x = int((width - width_text) / 2) + x
        text_y = int((height + height_text) / 2) + y
        cv2.putText(keyboard, text, (text_x,text_y),font_letter,font_scale,(255,0,0),font_th)
'''
 ______ ______
|      |      |
|      |      |
|______|______|
|      |      |
|      |      |
|______|______|
'''
def click_fin(cont):
    pass
    
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
    cv2.rectangle(keyboard,(x+th,y+th),(x+width-th,y+height-th),(255,0,0),-1)
        #cv2.rectangle(keyboard,(110,0),(210,100),(255,0,0),3)

key_clicked = '-1'
text_cli = ''
ind_key=[]
while True:

    ret,keyboard = cap.read()

    #print(text_size)
    keyboard = cv2.flip(keyboard,1)

    alphabet_letter = "q w e r t y u i o p [ ] \ a s d f g h j k l ; ' enter z x c v b n m , . @ shift".split()
    x_coords = []
    y_coords = []
    coords = []
    c = 0
    #max_lim = 1500
    x_add = 0
    line=0
    for i in range(0,768,90):
        coords.append([])
        for j in range(0,1366,95):
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

    fin_tot = [total[0:13]]
    fin_tot.append(total[13:25])
    fin_tot.append(total[25:36])
    fin_tot.append(total[36:41])
    fin_tot.append(total[41:46])
    fin_tot.append(total[46:51])


    start_num_x = 0
    start_num_y = y_coords[-1]+150
    c = 0
    count = 1

    for i in range(start_num_y,768, 90):
        count = 1
        coords.append([])
        for j in range(0,1366,85):
            if(c!=15):
                if count <= 5:
                    numbers_draw(j,i,num_side[c])
                    x_coords.append(j+x_add)
                    y_coords.append(i)
                    coords[line].append([j+x_add,i])
                    count+=1
                    c+=1
                else:
                    break
            else:
                break
        line+=1
        if c == 15:
            break

    cv2.putText(keyboard, "Slide finger for sliding operations", (j+100,start_num_y-30),cv2.FONT_HERSHEY_PLAIN,2,(120,120,0),2)
    cv2.rectangle(keyboard, (j+20,start_num_y-10),(j+300+550,start_num_y-105+450),(0,255,0),3)

    imgHSV= cv2.cvtColor(keyboard,cv2.COLOR_BGR2HSV)
    # create the Mask
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
    #morphology
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal=maskClose
    conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    if(len(conts)==1):

        x,y,w,h=cv2.boundingRect(conts[0])

        cx=x+w//2
        cy=y+h//2
        
        #circle in the midpoint of colored finger
        cv2.circle(keyboard, (cx,cy),2,(0,0,255),2)
        # rectangle around colored finger
        if x+w<x+50 and y+h< y+50:
            cv2.rectangle(keyboard,(x,y),(x+w,y+h),(255,0,0),2)
        else:
            cv2.rectangle(keyboard,(x,y),(x+50,y+50),(255,0,0),2)

        #centroid(int)
    
        

        ind_key,r_ind,c_ind = click_keys(cx,cy,x,y,w,h,coords)
        if r_ind != -1 and c_ind != -1:
            if len(ind_key) != 0:
                key_light(ind_key[0],ind_key[1],key_clicked)
                text_cli += fin_tot[r_ind][c_ind]
            
        #print(text_cli)
                  
    cv2.imshow("Keyboard",keyboard)

    if cv2.waitKey(2) == 13:
        break

cap.release()
cv2.destroyAllWindows()
