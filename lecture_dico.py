class Dictionnaire:
    def ouvrir_fichier(self):
        try:
            with open('liste_francais.txt', 'r') as f:
                contenu = f.read()
                mots = contenu.split()

            return mots
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
            return []
