from lecture_dico import Dictionnaire


class Occurrence:
  def __init__(self):
        self.array_word = []

    mon_dictionnaire = Dictionnaire()
    dico = mon_dictionnaire.ouvrir_fichier()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', 'é', 'è', 'à', 'ù', 'û', 'ô', 'â', 'î', 'ï', '-', ' ']



    def occurrence_letter(self):
        array_word = []
        dico = self.dico
        alphabet = self.alphabet
        for word in dico:
            for letter in word:
                if letter.lower() in alphabet:
                    array_word.append(letter.lower())
        array = array_word
        print(self.get_total_letters(alphabet, array))
    def get_total_letters(self, alphabet, array_word):
        total_letters = 0
        for letter in alphabet:

            total_letter = array_word.count(letter)
            total_letters = total_letters + array_word.count(letter)
            if(total_letter != 0):
                percentage = (total_letter / total_letters) * 100
            else:
                percentage = 0
            print(f"{letter} : {total_letter} - {percentage:.2f}%")
        return total_letters

        def diviser_en_paires(self):
        paires = []
        for i in range(len(self.array_word)-1):
            paires.append((self.array_word[i], self.array_word[i+1]))
        return paires