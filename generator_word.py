import random
from occurence_letter import Occurrence


class word_generator:
    def __init__(self):
        self.occurence = Occurrence()
        self.alphabet = self.occurence.alphabet
        self.array_proba_debut = self.occurence.get_percentage_first_letter()
        self.array_proba_fin = self.occurence.get_percentage_last_letter()
        self.array_proba_next_letter = self.occurence.next_letters()

    def choose_letter(self, probas):
        normalise_proba = [prob / sum(probas) for prob in probas]
        return random.choices(self.alphabet, weights=normalise_proba)[0]

    def generate_word(self, length_word, nb_words):
        array_words = []

        for _ in range(nb_words):
            word = ""
            first_letter = self.choose_letter(self.array_proba_debut)
            word += first_letter

            for _ in range(length_word - 2):
                active_letter = word[-1]
                next_proba = self.array_proba_next_letter.get(active_letter, [])
                if next_proba:
                    next_letter = self.choose_letter(next_proba)
                    word += next_letter
                else:
                    print(f"Aucun pourcentage_suivant défini pour '{active_letter}'")
                    break

            last_letter = self.choose_letter(self.array_proba_fin)
            word += last_letter
            array_words.append(word)

        return array_words
