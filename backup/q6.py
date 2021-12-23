# _________                             .__       .__     __    _________ .__                 .__                  ________           .____            _____              __         .__               
# \_   ___ \  ____ ______ ___.__._______|__| ____ |  |___/  |_  \_   ___ \|  |__ _____ _______|  |   ____   ______ \______ \   ____   |    |   _____ _/ ____\____   _____/  |______  |__| ____   ____  
# /    \  \/ /  _ \\____ <   |  |\_  __ \  |/ ___\|  |  \   __\ /    \  \/|  |  \\__  \\_  __ \  | _/ __ \ /  ___/  |    |  \_/ __ \  |    |   \__  \\   __\/  _ \ /    \   __\__  \ |  |/    \_/ __ \ 
# \     \___(  <_> )  |_> >___  | |  | \/  / /_/  >   Y  \  |   \     \___|   Y  \/ __ \|  | \/  |_\  ___/ \___ \   |    `   \  ___/  |    |___ / __ \|  | (  <_> )   |  \  |  / __ \|  |   |  \  ___/ 
#  \______  /\____/|   __// ____| |__|  |__\___  /|___|  /__|    \______  /___|  (____  /__|  |____/\___  >____  > /_______  /\___  > |_______ (____  /__|  \____/|___|  /__| (____  /__|___|  /\___  >
#         \/       |__|   \/              /_____/      \/               \/     \/     \/                \/     \/          \/     \/          \/    \/                 \/          \/        \/     \/ 
# Compte du nombre de consonnes dans un mot | 14 sept. 2021 | Charles De Lafontaine

def compte_nb_consonnes(mot):
    n_consonnes = 0
    voyelles = ['a', 'à', 'é', 'è', 'e', 'i', 'î', 'o', 'u', 'ù', 'y']

    for lettre in mot:
        if lettre not in voyelles:
            n_consonnes += 1
        
    return n_consonnes

if __name__ == "__main__":
    mot = input("Choisissez votre mot: ")

    print("Votre mot <", mot, "> possède", compte_nb_consonnes(mot), "consonnes.")
