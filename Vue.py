import tkinter as tk

class Vue(tk.Tk):
    def __init__(self, controleur):
        super().__init__()
        self.controleur = controleur
        self.title("Inventaire")
        self.geometry("970x1000")

        self._creer_widgets()

    def _creer_widgets(self):
        # Section du haut + titre
        self.frame_haut = tk.Frame(self, padx=10, pady=10)
        self.frame_haut.grid(row=0, column=0, columnspan=2, sticky="ew")
        tk.Label(self.frame_haut, text="Bonjour!", font=("Arial", 16)).pack()

        # Section de gauche + Inventaire + Admin + Paramètres + Déconnexion + Aide
        self.frame_gauche = tk.LabelFrame(self, text="Saisie", padx=10, pady=10)
        self.frame_gauche.grid(row=1, column=0, sticky="ns", padx=10, pady=10)

        # Bouton Inventaire
        tk.Button(self.frame_gauche, text="Inventaire", width=20, height=2).grid(row=0, column=0, pady=2, sticky="ew")
        self.frame_gauche.rowconfigure(1, weight=1)

        # Bouton Admin, Paramètres, Déconnexion, Aide
        tk.Button(self.frame_gauche, text="Admin", width=20, height=2).grid(row=2, column=0, pady=2, sticky="ew")
        tk.Button(self.frame_gauche, text="Paramètres", width=20, height=2).grid(row=3, column=0, pady=2, sticky="ew")
        tk.Button(self.frame_gauche, text="Déconnexion", width=20, height=2).grid(row=4, column=0, pady=2, sticky="ew")
        tk.Button(self.frame_gauche, text="Aide", width=20, height=2).grid(row=5, column=0, pady=2, sticky="ew")

        # Section de droite + Titre liste + Recherche + Ajouter + Information
        self.frame_droite = tk.LabelFrame(self, text="Liste", padx=10, pady=10)
        self.frame_droite.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # Titre fenêtre
        tk.Label(self.frame_droite, text="Emprunteurs",
                 font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Barre de recherche
        frame_recherche = tk.Frame(self.frame_droite)
        frame_recherche.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        tk.Label(frame_recherche, text="Rechercher (matricule) :        ").pack(side="left")
        self.entree_recherche = tk.Entry(frame_recherche)
        self.entree_recherche.pack(side="left", fill="x", expand=True, padx=(5, 0))
        tk.Button(frame_recherche, text="Rechercher", command=self.controleur.rechercher).pack(side="left")


        # Espace entre Saisie et liste - Ajouter un emprunteur, Information sur emprunteur
        frame_boutons = tk.Frame(self.frame_droite)
        frame_boutons.grid(row=2, column=0, sticky="n", padx=(0, 10))
        tk.Button(frame_boutons, text="Ajouter un emprunteur", width=20, height=2, command=self.controleur.ouvrir_ajout).pack(pady=2)
        tk.Button(frame_boutons, text="Information emprunteur", width=20, height=2).pack(pady=2)

        # Espace pour liste emprunteur ou liste équipement
        self.liste = tk.Listbox(self.frame_droite)
        self.liste.grid(row=2, column=1, sticky="nsew")

        # Ajustement de la page
        self.frame_droite.columnconfigure(1, weight=1)
        self.frame_droite.rowconfigure(2, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

    def afficher_message(self, texte):
        self.label_message.config(text=texte)

    def maj_liste(self, elements):
        self.liste.delete(0, tk.END)
        for e in elements:
            self.liste.insert(tk.END, e)

    def ouvrir_fenetre_ajout(self):
        fenetre = tk.Toplevel(self)
        fenetre.title("Ajout d'un emprunteur")
        fenetre.transient(self)  # reste au-dessus de la fenêtre principale
        fenetre.grab_set()  # bloque la fenêtre principale tant qu'elle est ouverte

        tk.Label(fenetre, text="Ajout d'un emprunteur",
                 font=("Arial", 16)).grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        tk.Label(fenetre, text="Matricule :").grid(row=1, column=0, sticky="w", padx=(20, 5), pady=2)
        entree_matricule = tk.Entry(fenetre)
        entree_matricule.grid(row=1, column=1, padx=(0, 20), pady=2)

        tk.Label(fenetre, text="Nom :").grid(row=2, column=0, sticky="w", padx=(20, 5), pady=2)
        entree_nom = tk.Entry(fenetre)
        entree_nom.grid(row=2, column=1, padx=(0, 20), pady=2)

        tk.Label(fenetre, text="Prénom :").grid(row=3, column=0, sticky="w", padx=(20, 5), pady=2)
        entree_prenom = tk.Entry(fenetre)
        entree_prenom.grid(row=3, column=1, padx=(0, 20), pady=2)

        tk.Label(fenetre, text="Statut :").grid(row=4, column=0, sticky="w", padx=(20, 5), pady=2)
        statut = tk.StringVar(value="etudiant")
        tk.OptionMenu(fenetre, statut, "etudiant", "professeur", "employé").grid(
            row=4, column=1, sticky="ew", padx=(0, 20), pady=2)

        label_erreur = tk.Label(fenetre, text="", fg="red")
        label_erreur.grid(row=5, column=0, columnspan=2)

        def valider():
            erreur = self.controleur.ajouter_emprunteur(
                entree_matricule.get(), entree_nom.get(),
                entree_prenom.get(), statut.get())
            if erreur:
                label_erreur.config(text=erreur)
            else:
                fenetre.destroy()

        tk.Button(fenetre, text="Ajouter", width=12, command=valider).grid(
            row=6, column=0, pady=10)
        tk.Button(fenetre, text="Annuler", width=12, command=fenetre.destroy).grid(
            row=6, column=1, pady=10)
