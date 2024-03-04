class Dictionnaire:
    def ouvrir_fichier(self):
        try:
            contenu = open('liste_francais.txt', 'r').read()
            mots = contenu.split()
            print(mots)
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")


