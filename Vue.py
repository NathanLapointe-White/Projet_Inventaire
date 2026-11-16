import tkinter as tk
class Vue():
    def __init__(self, controleur, modele):
        self.controleur = controleur
        self.modele = modele
        self.root = tk.Tk()
        self.cadre_principal = tk.Frame(self.root)
        self.cadre_principal.pack()
