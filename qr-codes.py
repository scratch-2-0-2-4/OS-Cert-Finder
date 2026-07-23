import platform
import sys

try:
    import qrcode
except ImportError:
    if platform.system() == "Windows":
        cmd = 'pip install "qrcode[pil]"'
    else:
        cmd = 'pip3 install "qrcode[pil]"'

    print(f"Erreur : La bibliothèque 'qrcode' n'est pas installée.")
    print(f"Veuillez l'installer en exécutant la commande suivante :\n")
    print(f"    {cmd}\n")
    sys.exit(1)

# Le reste de votre code
data = input("Certificat ? >>> ")

qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
qr.print_ascii(invert=True)
