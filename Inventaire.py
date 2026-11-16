import csv


class inventaire():
    FICHIER = "inventaire_equipements.csv"

    def lire_csv(self):
        with open(self.FICHIER, newline="", encoding="utf-8") as f:
            return list(csv.reader(f))

    def __init__(self):
        self.listeEquipement = self.lire_csv()

    def retourner_ligne(self, code):
        for i, ligne in enumerate(self.listeEquipement):
            if ligne and ligne[0] == code:
                return i
        return None

    def modifier_etat(self, etat, code):
        i = self.retourner_ligne(code)
        if i is None:
            return "Erreur"
        self.listeEquipement[i][2] = etat
        self.mettre_a_Jour_inventaire()

    def supprimer_equipement(self, ligne):
        del self.listeEquipement[ligne]
        self.mettre_a_Jour_inventaire()

    def ajouter_equipement(self, code, nom):
        self.listeEquipement.append([code, nom, "dispo"])
        self.mettre_a_Jour_inventaire()

    def mettre_a_Jour_inventaire(self):
        with open(self.FICHIER, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows(self.listeEquipement)

    def lister_pret_en_cours(self):
        listePrets = []
        for ligne in self.listeEquipement:
            if ligne and ligne[2] == "non-dispo":
                listePrets.append(ligne)
        return listePrets
