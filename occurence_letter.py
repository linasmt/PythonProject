from lecture_dico import Dictionnaire


class Occurrence:
    def __init__(self):
        mon_dictionnaire = Dictionnaire()
        self.dico = mon_dictionnaire.ouvrir_fichier()
        self.array_word = []
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z', 'é', 'è', 'à', 'ù', 'û', 'ô', 'â', 'î', 'ï', '-', ' ']

    def occurrence_letter(self):

        dico = self.dico
        for word in dico:
            for letter in word:
                if letter.lower() in self.alphabet:
                    self.array_word.append(letter.lower())
        print(self.get_percentage())

    def get_total_letters(self):
        total_letters = 0
        for letter in self.alphabet:
            total_letters = total_letters + self.array_word.count(letter)
        return total_letters

    def get_total_letter(self, letter):
        total_letter = self.array_word.count(letter)
        return total_letter

    def get_percentage(self):
        total_letters = self.get_total_letters()
        for letter in self.alphabet:
            total_letter = self.get_total_letter(letter)
            if total_letter != 0:
                percentage = (total_letter / total_letters) * 100
            else:
                percentage = 0
            print(f"{letter} : {total_letter} - {percentage:.2f}%")


    def diviser_en_paires(self):
        paires = []
        for i in range(len(self.array_word) - 1):
            paires.append((self.array_word[i], self.array_word[i + 1]))
        return paires
