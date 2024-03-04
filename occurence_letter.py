from lecture_dico import Dictionnaire


class Occurence:
    def occurence_letter(self):
        array_word = []
        mon_dictionnaire = Dictionnaire()
        dico = mon_dictionnaire.ouvrir_fichier()
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'w', 'x', 'y', 'z', '', 'é', 'è', 'à', 'ù', 'û', 'ô', 'â', 'î', 'ï', '-']
        for word in dico:
            for letter in word[0]:
                if letter in alphabet:
                    array_word.append(letter)
        print(array_word)
