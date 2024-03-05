import random
from occurence_letter import Occurrence

class MotGenerator:
    def __init__(self):
        self.occurence = Occurrence()
        self.alphabet = self.occurence.alphabet
        self.array_proba_debut = self.occurence.get_percentage_first_letter()
        self.array_proba_fin = self.occurence.get_percentage_last_letter()
        self.array_proba_nextletter = self.occurence.next_letters()

    def choisir_lettre(self, probas):
        poids_normalises = [prob / sum(probas) for prob in probas]
        return random.choices(self.alphabet, weights=poids_normalises)[0]

    def generer_mot(self, longueur_mot, nb_mots):
        array_words = []

        for _ in range(nb_mots):
            mot = ""
            premiere_lettre = self.choisir_lettre(self.array_proba_debut)
            mot += premiere_lettre

            for _ in range(longueur_mot - 2):
                lettre_actuelle = mot[-1]
                poids_suivant = self.array_proba_nextletter.get(lettre_actuelle, [])
                if poids_suivant:
                    lettre_suivante = self.choisir_lettre(poids_suivant)
                    mot += lettre_suivante
                else:
                    print(f"Aucun pourcentage_suivant défini pour '{lettre_actuelle}'")
                    break

            derniere_lettre = self.choisir_lettre(self.array_proba_fin)
            mot += derniere_lettre
            array_words.append(mot)

        return array_words
