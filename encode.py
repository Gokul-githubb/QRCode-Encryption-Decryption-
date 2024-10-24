import qrcode
data="Gokul"
qr=qrcode.QRCode(version=1,box_size=50,border=1)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_colour="red")
img.save("C:/Users/Home/OneDrive/Documents/Pictures/Saved Pictures/5.png")