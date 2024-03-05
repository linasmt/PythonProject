from occurence_letter import Occurrence
from GeneratorWord import MotGenerator
from word import Word

def main():
    word = MotGenerator()
    print(word.generer_mot(7))

if __name__ == '__main__':
    main()