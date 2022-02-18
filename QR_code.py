from asyncore import write
from os import access
import qrcode
import cv2 
import datetime

with open("Contact_data.txt") as lines:
    data_per_line = lines.read()

QR_img =qrcode.make(data_per_line)
QR_img.save("My_QR.png")





