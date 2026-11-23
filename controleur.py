from Modele import Modele
from Vue import Vue
import csv


class Controleur:
    def __init__(self):
        self.modele = Modele()
        self.vue = Vue(self)

    def demarrer(self):
        self.vue.mainloop()

    def information(self):
        pass

    def rechercher(self):
        texte = self.vue.entree_recherche.get()
        self.vue.maj_liste(self.modele.obtenir_liste())

    def lire_csv(self,fichier):
        with open(fichier, newline="", encoding="utf-8") as f:
            return list(csv.reader(f))

    def mettre_a_Jour_inventaire(self):
        with open(self.FICHIER, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows(self.listeEquipement)


if __name__ == "__main__":
    app = Controleur()
    app.demarrer()