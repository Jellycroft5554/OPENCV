import cv2
import numpy as np
import time

raw_video=cv2.VideoCapture("OPENCV\\utility\\video.mp4")

time.sleep(1)
count=0
background=0

for i in range(60): #first 60 frames
    return_val, background = raw_video.read()
    if return_val == False:
        continue

background=np.flip(background, axis=1) #x is 1 for horizontal flip

while(raw_video.isOpened()):
    return_val,img=raw_video.read()
    if not return_val: #if no frame is read
        break

    count +=1
    img=np.flip(img,axis=1)
    #HSV>RGB in colour detection
    hsv=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    lower_red1=np.array([140,40,40])
    upper_red1=np.array([100,255,25])

    lower_red2=np.array([155,40,40])
    upper_red2=np.array([180,255,255])

    mask1=cv2.inRange(hsv,lower_red1,upper_red1)
    mask2=cv2.inRange(hsv,lower_red2,upper_red2)

    mask1=mask1+mask2
    red_mask=cv2.bitwise_or(mask1,mask2)
                            
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    mask1=cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations=1)#extending detected region

    #inverting the mask

    mask2=cv2.bitwise_not(mask1)
    result1=cv2.bitwise_and(background,background,mask=mask1)
    result2=cv2.bitwise_and(img,img,mask=mask2)
    final_output=cv2.addWeighted(result1,1,result2,1,0)
    cv2.imshow("invisible boy",final_output)
    if cv2.waitKey(5)==ord("q"):
        break