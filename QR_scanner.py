from ast import While
import cv2
from pyzbar.pyzbar import decode
import numpy as np


def Scanning_func():
 webcam=cv2.VideoCapture(0)
 while True:
    other, frame= webcam.read()
    decoded_QR = decode(frame)   
    try:
        string_decoded_QR=decoded_QR[0][0].decode("utf-8")
        print(string_decoded_QR)
    except:
        pass    
    cv2.imshow("QR_scanner.py", frame)
    key=cv2.waitKey(1)

    if key == 27:
        break

 webcam.release()
 cv2.destroyAllWindows()


Scanning_func()

