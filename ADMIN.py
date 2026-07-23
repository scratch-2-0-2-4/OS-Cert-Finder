import re
import hashlib

MDP_LHF_vvm = "e8e7f8c8f8c8e8c8e8c8e8c8e8c8e8c8e8c8e8c8e8c8e8c8e8c8e8c8e8c8e8"

pattern = r"^[A-Z]{3}-\d{3}-[a-z]{3}$"
admin = input("Certificat >>> ")

if re.fullmatch(pattern, admin):
    if admin == "LHF-557-vvm":
        mdp = input("Mot de Passe ? >>> ")
        mdp_hash = hashlib.sha256(mdp.encode()).hexdigest()
        
        if MDP_LHF_vvm == mdp_hash:
            print("\033[32m ✔ Ok\033[0m")
            print("Mode ADMIN à venir")
        else:
            print("\033[31m ✖ Mot de Passe invalide \033[0m")
    else:
        print("\033[31m ✖ Non-trouvé. \033[0m")
else:
    print("\033[31m ✖ Format invalide. Format correct : \033[1m ABC-123-def \033[0m \033[0m")
