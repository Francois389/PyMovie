class Tableur:
    def __init__(self, path):
        self.path = path

    def get_entete(self)->list[str]:
        pass

    def get_rows(self)->list[list]:
        pass

    def get_content_colum(self, colonne: int | str)->list:
        """
        Renvoie les valeurs d'une colonne
        :param colonne: L'index de la colonne
        :return: Une liste de valeurs
        """
        pass

    def get_index_of(self, colonne: str)->int:
        """
        Renvoie l'index d'une colonne à partir de son nom
        renvoie -1 si la colonne n'existe pas
        :param colonne: Le nom de la colonne
        :return: L'index de la colonne
        """
        pass
