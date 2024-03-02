import qrcode
from qrcode.constants import ERROR_CORRECT_L

qr = qrcode.QRCode(
    version = 4,
    error_correction=ERROR_CORRECT_L,
    box_size=3,
    border=3
)

data_qrcode = input('Entrez le lien ou le texte que vous souhaiter afficher dans votre QRcode : ')

qr.add_data(data_qrcode)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')