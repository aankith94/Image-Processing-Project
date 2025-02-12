# Color Picker

import cv2
import numpy as np

def cross(x):
    pass



# Blank Images
img = np.zeros([300,512,3],np.uint8)
cv2.namedWindow("color Picker")

# Create Switch
s1 = "0:OFF\n1:ON"
cv2.createTrackbar(s1, "color Picker",0,1,cross)

# Creating for 

# Creating Trackbars for Adjusting Colors
cv2.createTrackbar("R","color Picker",0,255,cross)
cv2.createTrackbar("G","color Picker",0,255,cross)
cv2.createTrackbar("B","color Picker",0,255,cross)



while True:
    cv2.imshow("color Picker",img)
    k= cv2.waitKey(1) & 0xFF
    if k == 27: # for exit
        break


    # now get trackbar position
    s = cv2.getTrackbarPos(s1,"color Picker")
    r = cv2.getTrackbarPos("R","color Picker")
    g = cv2.getTrackbarPos("G","color Picker")
    b = cv2.getTrackbarPos("B","color Picker")
    
    if s == 0:
        img[:]  = 0
    else:
        img[:] = [r,g,b]
        
cv2.destroyAllWindows()
    