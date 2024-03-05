class Dictionnaire:
    def open_file(self):
        try:
            with open('liste_francais.txt', 'r') as f:
                content = f.read()
                mots = content.split()

            return mots
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
            return []
