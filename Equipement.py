from enum import Enum

class Etat(Enum):
    DISPO = "disponible"
    NON_DISPO = "non-disponible"
    EN_PANNE = "en panne"

class equipement():
    FICHIER = "inventaire_equipements.csv"


    def __init__(self,code,info,etat):
        self.code = code
        self.info = info
        self.etat = Etat(etat)
        self.historique = []

    def modifier_etat(self, etat):
       self.etat = etat

    def modifier_code(self, code):
        self.code = code

    def modifierEtat(self, etat):
        self.etat = etat

    def ajouterHistorique(self,emprunt):
        self.historique.append(emprunt)
