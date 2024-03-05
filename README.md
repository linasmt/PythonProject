TP : SLM
Création d'un générateur de mot aléatoire à consonnance française, sur la base d'une liste de mots français
1 : Obtention d'une liste de mots français (et traitement, si nécessaire)
2 : Etablissement d'un tableau de probabilité de N dimensions pour chaque lettre (On considère "début de mot" et "fin de mot" comme des caractères)
3 : Utilisation de ce tableau pour générer des mots à consonnance française 

La génération de mot doit évidemment être séparée de l'établissement du tableau. On ne veut pas le ré-établir à chaque lancement du générateur. Donc, le tableau doit être enregistré.

Par : Bedos Chulee et Smati Lina