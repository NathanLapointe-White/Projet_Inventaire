from Modele import Modele
from Vue import Vue

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

if __name__ == "__main__":
    app = Controleur()
    app.demarrer()

