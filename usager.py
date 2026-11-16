from enum import Enum
class Status(Enum):
    ETUDIANT = "etudiant"
    PROFESSEUR = "professeur"
    EMPLOYE = "employé"

class usager():
    def __init__(self,matricule,nom,prenom,status):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.status = Status(status)
        self.historique = []
        self.emprunts = 0

    def modifierNom(self,nom):
        self.nom = nom

    def modifierPrenom(self,prenom):
        self.prenom = prenom

    def modifierMatricule(self,matricule):
        self.matricule = matricule

    def modifierStatus(self,status):
        self.status = status

    def ajouterEmprunt(self):
        if self.emprunts<=3:
            self.emprunts+=1
        else:
            return "Emprunts maximum atteint !"

    def ajouterHistorique(self,emprunt):
        self.historique.append(emprunt)

    def retirerEmprunt(self):
        if self.emprunts >0:
            self.emprunts -= 1
        else:
            return "Aucun emprunt en cours"