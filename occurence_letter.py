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
            for letter in word:
                if letter.lower() in alphabet:
                    self.array_word.append(letter.lower())

    def diviser_en_paires(self):
        paires = []
        for i in range(len(self.array_word)-1):
            paires.append((self.array_word[i], self.array_word[i+1]))
        return paires
