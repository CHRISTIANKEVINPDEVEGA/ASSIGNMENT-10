from asyncore import write
from fileinput import close
from os import access
import qrcode
import cv2 


QR = open("Contact_data.txt","r").read()
qr=qrcode.make(QR)
qr.save("MY_QR.png")
