from Equipement import equipement
from Usager import usager


class Emprunt():
    def __init__(self, un_usager: usager, un_equipement: equipement):
        self.usager = un_usager
        self.equipement = un_equipement

