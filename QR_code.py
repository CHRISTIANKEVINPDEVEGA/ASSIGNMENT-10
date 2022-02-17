import qrcode
import cv2 

txt=open("Contact_data.txt").read()
img = qrcode.make(txt)  
img.save("some_file.png")

QR_val= cv2.QRCodeDetector()

RetVal,Points,Straight_qrcode=QR_val.detectAndDecode(cv2.imread("some_file.png"))
print(RetVal)
