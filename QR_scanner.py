from ast import While
import cv2
from pyzbar.pyzbar import decode
from pyzbar import pyzbar
import numpy as np


def Scanning_func():
 webcam=cv2.VideoCapture(0)
 webcam.set(3,640)
 webcam.set(4,480)
 while True:
    other, frame= webcam.read()
    decoded_QR = pyzbar.decode(frame)   
    for QR_code in decoded_QR:
        string_decoded_QR = QR_code.data.decode("utf-8")
        print(string_decoded_QR)
        x_value, y_value , width, height = QR_code.rect
        cv2.rectangle(frame, (x_value, y_value),(x_value+width, y_value+height), (300, 0, 280), 10)

    cv2.imshow("QR_scanner.py", frame)
    key=cv2.waitKey(1)

    if key == 27:
        break

 webcam.release()
 cv2.destroyAllWindows()


Scanning_func()

