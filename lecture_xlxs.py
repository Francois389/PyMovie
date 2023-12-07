import pandas as pd
from lecture_tableur import Tableur


class TableurXLSX(Tableur):
    def __init__(self, path):
        super().__init__(path)

    def get_entete(self)->list[str]:
        """
        Renvoie les entêtes du tableur
        :return: Une liste de str
        """
        return pd.read_excel(self.path).columns.tolist()

    def get_rows(self)->list[list]:
        return pd.read_excel(self.path).values.tolist()

    def get_content_colum(self, colonne: int | str)->list:
        """
        Renvoie les valeurs d'une colonne
        :param colonne: L'index de la colonne
        :return: Une liste de valeurs
        """
        indice: int = colonne
        if type(colonne) is str:
            indice = self.get_index_of(colonne)
        return pd.read_excel(self.path).iloc[:, indice].tolist()

    def get_index_of(self, colonne: str)->int:
        """
        Renvoie l'index d'une colonne à partir de son nom
        renvoie -1 si la colonne n'existe pas
        :param colonne: Le nom de la colonne
        :return: L'index de la colonne
        """
        entete = self.get_entete()
        for i, j in enumerate(entete):
            if j == colonne:
                return i
        return -1


if __name__ == "__main__":
    tab = TableurXLSX("test.xlsx")
    print(tab.get_entete())
    print(tab.get_content_colum(0))
    print(tab.get_content_colum("Titre"))
    print(tab.get_index_of("Titre"))
