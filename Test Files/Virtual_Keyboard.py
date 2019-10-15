import cv2
import numpy as np


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
        height = 90

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

    


while True:

    ret,keyboard = cap.read()

    #print(text_size)


    alphabet_letter = "q w e r t y u i o p [ ] \ a s d f g h j k l ; ' enter z x c v b n m , . @ shift".split()
    x = []
    y = []
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
                    x.append(j+x_add)
                    y.append(i)
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

    for i in alphabet_letter:
        total.append(i)
    for i in num_side:
        total.append(i)

    start_num_x = 0
    start_num_y = y[-1]+150
    c = 0
    count = 1

    for i in range(start_num_y,768, 90):
        count = 1
        coords.append([])
        for j in range(0,1366,85):
            if(c!=15):
                if count <= 5:
                    numbers_draw(j,i,num_side[c])
                    x.append(j+x_add)
                    y.append(i)
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

    '''
    pos_x = cent_pos_5
    pos_y = cent_pos_y

    for i in range(len(coords)):
        for j in range(len(i)):
            if pos_x > coords[i][j][0] and pos_x < coords[i][j+1][0]:
                if pos_y >

    '''
                  
    cv2.imshow("Keyboard",keyboard)

    if cv2.waitKey(2) == 13:
        break

cap.release()
cv2.destroyAllWindows()
