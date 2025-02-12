# Screen Recording using opencv and numpy
import cv2 as c
import numpy as np
import pyautogui as p

# Create Resolution
rs = p.size()

# filename in which we store Recording
fn = input("Please Enter any File name and path: ")
# Fix the frame rate
fps = 60.0

fourcc = c.VideoWriter_fourcc(*'XVID')
record = c.VideoWriter(fn,fourcc,fps,rs)

# Create Recording Module
c.namedWindow("Live_Recording",c.WINDOW_NORMAL)
c.resizeWindow("Live_Recording",(600,400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = c.cvtColor(f,c.COLOR_BGR2RGB)
    record.write(f)
    c.imshow("Live_Recording",f)
    if c.waitKey(1) == ord('q'):
        break
    
record.release()
c.destroyAllWindows()


