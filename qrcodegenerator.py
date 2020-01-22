from pyqrcode import QRCode
# url = QRCode("https://www.google.com/")
# # url.svg('uca-url.svg', scale=8)
# print(url.terminal(quiet_zone=1))

number = QRCode("type whatever you want")
number.png('big-number.png', scale=20)
