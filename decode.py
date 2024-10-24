from pyzbar.pyzbar import decode
from PIL import Image
img=img.open("C:\Users\Home\OneDrive\Documents\Pictures\Saved Pictures\gokul1qr.png")
res=decode(img)
print(res)