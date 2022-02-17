import qrcode
txt=open("Contact_data.txt").read()
img = qrcode.make(txt)
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
