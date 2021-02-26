import imutils
import cv2 ;
def detect(c):
    shape = "undifined";
    length=cv2.arcLength(c, True)
    approx=cv2.approxPolyDP(c, 0.04*length, True)
    nop = len(approx)
    if nop==3:
        shape="triangle"
    elif nop==4:
        (x,y,w,h)=cv2.boundingRect(approx)
        s=float(w)/float(h)
        shape="square" if s>=0.95 and s<=1.05 else "rectangle"
    elif nop ==5 :
        shape="pentagon"
    else:
        shape="circle"
    return shape
    #reading the image
img =cv2.imread('image.png')

gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

blur=cv2.GaussianBlur(gray, (5,5), 0)
thresh=cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)[1]
cnts =cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)

for c in cnts: 
    cv2.drawContours(img, [c], -1, (0,0,255),2)
    M =cv2.moments(c)
    '''cx=int((M["m10"]/M["m00"]))
    cy=int((M["m01"]/M["m00"]))'''
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        # set values as what you need in the situation
        cx, cy = 0, 0
    shape=detect(c)
    cv2.putText(img, shape, (cx,cy), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
cv2.imshow('CONT',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

