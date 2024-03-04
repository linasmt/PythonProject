from lecture_dico import Dictionnaire


class Occurrence:
    def __init__(self):
        self.array_word = []

    def occurrence_letter(self):
        mon_dictionnaire = Dictionnaire()
        dico = mon_dictionnaire.ouvrir_fichier()
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', 'é', 'è', 'à', 'ù', 'û', 'ô', 'â', 'î', 'ï', '-']

        for word in dico:
            cleaned_word = ''.join(char.lower() for char in word if char.lower() in alphabet)
            if cleaned_word:
                self.array_word.append(cleaned_word)

    def diviser_en_paires(self):
        paires = []
        for mot in self.array_word:
            for i in range(0, len(mot) - 1):
                paires.append((mot[i], mot[i + 1]))
            if len(mot) % 2 != 0:
                paires.append((mot[-1], ' '))
        return paires
