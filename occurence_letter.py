from collections import defaultdict
from lecture_dico import Dictionnaire

class Occurrence:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', 'é', 'è', 'à', 'ù', 'û', 'ô', 'â', 'î', 'ï', '-']

    def __init__(self):
        my_dictionnary = Dictionnaire()
        self.dico = self.dico = my_dictionnary.open_file()
        self.array_word = []
        self.array_proba_first = []
        self.array_proba_last = []
        self.array_proba_next_letter = []

    def get_all_letters(self):
        dico = self.dico
        for word in dico:
            for letter in word:
                if letter.lower() in self.alphabet:
                    self.array_word.append(letter.lower())
        return self.array_word

    def get_total_letters(self):
        total_letters = 0
        for letter in self.alphabet:
            total_letters += self.array_word.count(letter)
        return total_letters

    def get_total_letter(self, letter):
        return self.array_word.count(letter)

    def get_percentage(self):
        total_letters = self.get_total_letters()
        for letter in self.alphabet:
            total_letter = self.get_total_letter(letter)
            if total_letter != 0:
                percentage = (total_letter / total_letters) * 100
            else:
                percentage = 0
            print(f"{letter} : {total_letter} - {percentage:.2f}%")

    def split_into_pairs(self):
        pairs = self.get_all_letters()
        length = len(self.array_word)
        for i in range(length - 1):
            pairs.append((self.array_word[i], self.array_word[i + 1]))
        return pairs

    def get_percentage_first_letter(self):

        array = [mot[0] for mot in self.dico]
        total_letters = len(array)
        self.array_proba_first = []
        for letter in self.alphabet:
            total_letter = array.count(letter)
            percentage = (total_letter / total_letters) * 100
            self.array_proba_first.append(round(percentage, 2))
        return self.array_proba_first

    def get_percentage_last_letter(self):
        array = [mot[-1] for mot in self.dico]
        total_letters = len(array)
        self.array_proba_last = []
        for letter in self.alphabet:
            total_letter = array.count(letter)
            percentage = (total_letter / total_letters) * 100
            self.array_proba_last.append(round(percentage, 2))
        return self.array_proba_last

    def next_letters(self):
        tableau_lettres = defaultdict(list)
        for pair in self.split_into_pairs():
            if len(pair) == 2:
                first_letter, second_letter = pair
                tableau_lettres[first_letter].append(second_letter)
            else:
                first_letter = pair
                tableau_lettres[first_letter].append(first_letter)
        result = {}

        for key, value in tableau_lettres.items():
            next_letters_counts = []
            total_occurrences = len(value)
            unique_values = sorted(set(value))
            for letter in self.alphabet:
                if letter in unique_values:
                    count = value.count(letter)
                    percentage = round((count / total_occurrences) * 100, 2)
                    next_letters_counts.append(percentage)
                else:
                    next_letters_counts.append(0.0)
            result[key] = next_letters_counts
        return result

if __name__ == "__main__":
    occurrence = Occurrence()
    occurrence.get_all_letters()
    array_next_letters = occurrence.next_letters()
    for key, value in sorted(array_next_letters.items()):
        print(f"{key.upper()} = {value}")
