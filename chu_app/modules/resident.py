class Patient:
    """Classe Patient"""

    def __init__(self, nom, prenom, age, date_entree, date_sortie):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.date_entree = date_entree
        self.date_sortie = date_sortie
    
    def save_patient_to_db(self):
        """
        Enregistrer les patient en base de données
        """
        print("Patient enregistré en base")

    def count_patients_in_db(self):
        """
        Compte les patients inscrits en base de données
        """
        pass

    # Notes chef de service
    def entrer_a_l_hopital():
        pass

    def sortir_de_l_hopital():
        pass


class RH:
    """Classe RH"""
    pass

    # Notes chef de service
    def debuter_CDD_CDI():
        pass

    def quitter_CDD_CDI():
        pass