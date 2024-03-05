import random

from occurence_letter import Occurrence
class Word:
    def __init__(self):
        self.occurence = Occurrence()
        self.dico = self.occurence.dico
        self.alphabet = self.occurence.alphabet
        self.alphabet = self.occurence.alphabet
        self.array_proba_debut = self.occurence.array_proba_debut
        self.array_proba_fin = self.occurence.array_proba_fin
        self.array_proba_nextletter = self.occurence.array_proba_nextletter

    def generer_mot(self, longueur):
        if longueur <= 0:
            return ""

        # Choisir la première lettre en fonction du pourcentage_debut
        premiere_lettre = random.choices(self.alphabet, weights=self.array_proba_debut)[0]
        mot = premiere_lettre

        # Choisir les lettres suivantes en fonction du pourcentage_suivant
        for _ in range(1, longueur - 1):
            lettre_actuelle = mot[-1]
            if lettre_actuelle in self.array_proba_nextletter:
                poids_suivant = self.array_proba_nextletter[lettre_actuelle]
                lettre_suivante = random.choices(self.alphabet, weights=poids_suivant)[0]
                mot += lettre_suivante
            else:
                # Gérer le cas où la lettre actuelle n'a pas de pourcentage_suivant défini
                print(f"Aucun pourcentage_suivant défini pour '{lettre_actuelle}'")
                break

        # Choisir la dernière lettre en fonction du pourcentage_fin
        derniere_lettre = random.choices(self.alphabet, weights=self.array_proba_fin)[0]
        mot += derniere_lettre

        return mot


