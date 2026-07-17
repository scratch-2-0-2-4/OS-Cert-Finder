import requests
import os
import time
import re



Certificat = input("Rechercher un certificat (ex : ABC-123-def) >>> ")

if re.fullmatch(r"^[A-Z]{3}-\d{3}-[a-z]{3}$", Certificat):
  if Certificat == "LHF-557-vvm":
    print(f"Certificat n° \033[1m{Certificat}\033[0m \033[32m ✔ Ok\033[0m")
    print("Créateur : \033[1m Scratch_2_0_2_4\033[0m \033[34m vérifié \033[0m")
    print("Nom de l'OS : \033[1m Scratch.OS X\033[m")
  elif Certificat == "ABC-123-def":
     print(f"Certificat n° \033[1m{Certificat}\033[0m \033[33m certificat exemple \033[0m")
  else :
     print(f"\033[31m ✖ Le certificat \033[1m{Certificat}\033[m \033[31m n'existe pas.\033[0m")
elif Certificat == "ADMIN" :
  print("ADMIN Mode")
  ADMIN = input("Administration >>> ")
elif Certificat == "help" :
  print("Commandes : ")
  print("• Recherche de certificats")
else:
    print("\033[31m ✖ Format invalide. Format correct : \033[1m ABC-123-def \033[0m \033[0m")
