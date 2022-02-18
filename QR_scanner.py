from ast import While
from subprocess import call
import cv2
from pyzbar.pyzbar import decode
from pyzbar import pyzbar
import numpy as np
import datetime

def Scanning_func():
 webcam=cv2.VideoCapture(0)
 webcam.set(3,640)
 webcam.set(4,480)
 while True:
    DATE_TIME_saved = datetime.datetime.now()
    other, Scanner_img_cap= webcam.read()
    decoded_QR = pyzbar.decode(Scanner_img_cap)   
    for QR_code in decoded_QR:
        string_decoded_QR = QR_code.data.decode("utf-8")
        print(string_decoded_QR + "\n" + "Scanned on :" + DATE_TIME_saved.strftime("%c"))
        pts_poly = np.array([QR_code.polygon],np.int32)
        pts_poly =pts_poly.reshape((-1,1,2))
        cv2.polylines(Scanner_img_cap,[pts_poly],True,(200,0,100),5)
        pts_for_letter = QR_code.rect
        cv2.putText(Scanner_img_cap, string_decoded_QR, (pts_for_letter[0],pts_for_letter[1]), cv2.FONT_ITALIC, 0.9 ,(250,2,59), 2)
        with open("Contact Tracing.txt", mode ='a') as contact_file_storage:
            contact_file_storage.write("Contact have been saved: \n" + string_decoded_QR)
            contact_file_storage.write("\n"+"\n"+"\n")
            contact_file_storage.write(f"Contact was saved and scanned on:\n" + DATE_TIME_saved.strftime("%c"))
    cv2.imshow("QR_scanner.py", Scanner_img_cap)
    key=cv2.waitKey(1)

    if key == 27:
        break

 webcam.release()
 cv2.destroyAllWindows()

Scanning_func()

