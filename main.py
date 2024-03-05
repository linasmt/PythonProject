from generator_word import word_generator

def main():
    word = word_generator()
    print(word.generate_word(7, 10))

if __name__ == '__main__':
    main()