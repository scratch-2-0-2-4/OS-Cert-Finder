import re
import os

pattern = r"^[A-Z]{3}-\d{3}-[a-z]{3}$"
admin = input("Certificat >>> ")

MDP_LHF = os.getenv('MDP_LHF_VVM')

if re.fullmatch(pattern, admin):
    if admin == "LHF-557-vvm":
        mdp = input("Mot de Passe ? >>> ")
        if MDP_LHF == mdp:
            print("Ok")
        else:
            pass
    else:
        pass
else:
    pass
