import qrcode
from qrcode.constants import ERROR_CORRECT_L

qr = qrcode.QRCode(
    version = 4,
    error_correction=ERROR_CORRECT_L,
    box_size=3,
    border=3
)

qr.add_data('Merci d\'avoir scanné mon QRcode')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')