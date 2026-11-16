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

        tk.Button(self.frame_gauche, text="Inventaire", width=20, height=2).grid(row=0, column=0, pady=2, sticky="ew")

        self.frame_gauche.rowconfigure(1, weight=1)

        tk.Button(self.frame_gauche, text="Admin", width=20, height=2).grid(row=2, column=0, pady=2, sticky="ew")
        tk.Button(self.frame_gauche, text="Paramètres", width=20, height=2).grid(row=3, column=0, pady=2, sticky="ew")
        tk.Button(self.frame_gauche, text="Déconnexion", width=20, height=2).grid(row=4, column=0, pady=2, sticky="ew")
        tk.Button(self.frame_gauche, text="Aide", width=20, height=2).grid(row=5, column=0, pady=2, sticky="ew")

        # Section de droite + Titre liste + Recherche + Ajouter + Information
        self.frame_droite = tk.LabelFrame(self, text="Liste", padx=10, pady=10)
        self.frame_droite.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        tk.Label(self.frame_droite, text="Emprunteurs",
                 font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        frame_recherche = tk.Frame(self.frame_droite)
        frame_recherche.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        tk.Label(frame_recherche, text="Rechercher (matricule) :        ").pack(side="left")
        self.entree_recherche = tk.Entry(frame_recherche)
        self.entree_recherche.pack(side="left", fill="x", expand=True, padx=(5, 0))
        self.entree_recherche.bind("<KeyRelease>",
                                   lambda event: self.controleur.rechercher())

        frame_boutons = tk.Frame(self.frame_droite)
        frame_boutons.grid(row=2, column=0, sticky="n", padx=(0, 10))

        tk.Button(frame_boutons, text="Ajouter un emprunteur", width=20, height=2).pack(pady=2)
        tk.Button(frame_boutons, text="Information emprunteur", width=20, height=2).pack(pady=2)

        self.liste = tk.Listbox(self.frame_droite)
        self.liste.grid(row=2, column=1, sticky="nsew")

        # Ajustement de la page
        self.frame_droite.columnconfigure(1, weight=1)
        self.frame_droite.rowconfigure(2, weight=1)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)



