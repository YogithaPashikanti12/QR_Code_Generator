import qrcode
data="https://www.indiabix.com/verbal-reasoning"
img= qrcode.make(data)
img.save("my_qr.png")