class Modele:
    FICHIER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "liste_emprunter.csv")

    def __init__(self):
        self.usagers = []
        self.charger_usagers()
    def charger_usagers(self):
        try:
            with open(self.FICHIER, newline="", encoding="utf-8") as f:
                for ligne in csv.reader(f):
                    if len(ligne) != 4:
                        continue
                    matricule, nom, prenom, statut = ligne
                    try:
                        self.usagers.append(usager(matricule, nom, prenom, statut))
                    except ValueError:
                        continue
        except FileNotFoundError:
            pass

    def sauvegarder_usagers(self):
        with open(self.FICHIER, "w", newline="", encoding="utf-8") as f:
            ecrivain = csv.writer(f)
            for u in self.usagers:
                ecrivain.writerow([u.matricule, u.nom, u.prenom, u.status.value])

    def ajouter_usager(self, matricule, nom, prenom, statut):
        if not matricule.strip() or not nom.strip() or not prenom.strip():
            raise ValueError("Tous les champs sont obligatoires")
        if any(u.matricule == matricule for u in self.usagers):
            raise ValueError("Ce matricule existe déjà")
        self.usagers.append(usager(matricule, nom, prenom, statut))
        self.sauvegarder_usagers()

    def obtenir_liste(self, filtre=""):
        return [
            f"{u.matricule}   {u.nom}   {u.prenom}   {u.status.value}"
            for u in self.usagers
            if filtre in u.matricule
        ]
