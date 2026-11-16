import csv
class inventaire():
    FICHIER = "inventaire_equipements.csv"
    def lireCsv(self):
        with open(self.FICHIER, newline="",encoding="utf-8") as f:
            return list(csv.reader(f))

    def __init__(self):
        self.listeEquipement = self.lireCsv()

    def retournerLigne(self,code):
        for i, ligne in enumerate(self.listeEquipement):
            if ligne[0] == code :
                return i
        return None

    def modifierEtat(self,etat,ligne):
        self.listeEquipement[ligne][2] = etat
        self.mettreAJourInventaire()

    def supprimerEquipement(self,ligne):
        del self.listeEquipement[ligne]
        self.mettreAJourInventaire()

    def ajouterEquipement(self,code,nom):
        self.listeEquipement.append([code,nom,"dispo"])
        self.mettreAJourInventaire()

    def mettreAJourInventaire(self):
        with open(self.FICHIER,"w",newline="",encoding="utf-8") as f:
            csv.writer(f).writerows(self.listeEquipement)