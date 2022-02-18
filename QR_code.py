from asyncore import write
from os import access
import qrcode
import cv2 
import datetime

txt=open("Contact_data.txt").read()
img = qrcode.make(txt)  
img.save("some_file.png")
 