import platform
import random
import string
import sys

try:
    import qrcode
except ImportError:
    if platform.system() == "Windows":
        cmd = 'pip install "qrcode[pil]"'
    else:
        cmd = 'pip3 install "qrcode[pil]"'

    print("Erreur : La bibliothèque 'qrcode' n'est pas installée.")
    print("Veuillez l'installer en exécutant la commande suivante :\n")
    print(f"    {cmd}\n")
    sys.exit(1)


def afficher_qr(data):
    """Affiche un QR code ASCII directement dans le terminal."""
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr.print_ascii(invert=True)


def generer_code():
    ABC = "".join(random.choice(string.ascii_uppercase) for _ in range(3))
    _123 = "".join(random.choice(string.digits) for _ in range(3))
    ghi = "".join(random.choice(string.ascii_lowercase) for _ in range(3))
    return f"{ABC}-{_123}-{ghi}"


code_genere = generer_code()
print(code_genere)
print("/n")
afficher_qr(code_genere)
