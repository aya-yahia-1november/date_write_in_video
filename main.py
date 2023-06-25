import cv2
import datetime
cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        text="width"+str(cap.get(3))+"heigh"+str(cap.get(4))
        date=str(datetime.datetime.now())
        frame=cv2.putText(frame,text,(10,50),font,1,(128,0,128),2)
        frame=cv2.putText(frame,date,(10,100),font,1,(255,240,245),2)
        cv2.imshow("frame_date",frame)
        if cv2.waitKey(1)==ord("q"):
            break
    else:
        break

cap.read()
cv2.destroyAllWindows()