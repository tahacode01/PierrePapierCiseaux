import random

choix = ["pierre", "papier", "ciseaux"]

def resultat(joueur, ordi):
    if joueur == ordi:
        return "Égalité !"
    elif (joueur == "pierre" and ordi == "ciseaux") \
         or (joueur == "papier" and ordi == "pierre") \
         or (joueur == "ciseaux" and ordi == "papier"):
        return "Tu as gagné 🎉"
    else:
        return "L'ordinateur a gagné 😢"

while True:
    joueur = input("Pierre, papier ou ciseaux ? (q pour quitter) : ").lower()
    if joueur == "q":
        break
    if joueur not in choix:
        print("Choix invalide, réessaye.")
        continue

    ordi = random.choice(choix)
    print("Ordinateur a choisi :", ordi)
    print(resultat(joueur, ordi))
