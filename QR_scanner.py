from ast import While
import cv2
from pyzbar.pyzbar import decode


def Scanning_func():
 webcam=cv2.VideoCapture(0)

 while True:
    other, frame= webcam.read()
    decoded_QR = decode(frame)     
    try:
        print(decoded_QR[0][0] )
    except:
        pass
    cv2.imshow("QR_scanner.py", frame)

    key=cv2.waitKey(1)

    if key == 27:
        break

 webcam.release()
 cv2.destroyAllWindows()

Scanning_func()

