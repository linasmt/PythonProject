import random
from generator_word import word_generator

def main():

    word = word_generator()
    nb_words = 10
    longueur_mot = []
    for i in range(1, nb_words + 1):
        longueur_mot.append(random.randint(3, 10))

    for i in range(len(longueur_mot)):
        print(word.generate_word(longueur_mot[i], nb_words))


main()