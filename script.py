import platform
import random
import re
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


def generer_code():
    ABC = "".join(random.choice(string.ascii_uppercase) for _ in range(3))
    _123 = "".join(random.choice(string.digits) for _ in range(3))
    ghi = "".join(random.choice(string.ascii_lowercase) for _ in range(3))
    return f"{ABC}-{_123}-{ghi}"


def afficher_qr(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr.print_ascii(invert=True)


Certificat = input("Rechercher un certificat (ex : ABC-123-def) >>> ")

if re.fullmatch(r"^[A-Z]{3}-\d{3}-[a-z]{3}$", Certificat):
    if Certificat == "LHF-557-vvm":
        print(f"Certificat n° \033[1m{Certificat}\033[0m \033[32m ✔ Ok\033[0m")
        print("Créateur : \033[1m Scratch_2_0_2_4\033[0m \033[34m vérifié \033[0m")
        print("Nom de l'OS : \033[1m Scratch.OS X\033[m\n")
        afficher_qr(Certificat)

    elif Certificat == "ABC-123-def":
        print(
            f"Certificat n° \033[1m{Certificat}\033[0m \033[33m certificat exemple \033[0m\n"
        )
        # Affichage du QR code pour l'exemple
        afficher_qr(Certificat)

    else:
        print(
            f"\033[31m ✖ Le certificat \033[1m{Certificat}\033[m \033[31m n'existe pas.\033[0m"
        )

elif Certificat == "Generate code":
    nouveau_code = generer_code()
    print(f"Code généré : {nouveau_code}\n")
    afficher_qr(nouveau_code)

else:
    print("\033[31m ✖ Format invalide. Format correct : \033[1m ABC-123-def \033[0m \033[0m")
