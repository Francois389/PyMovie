import ezodf as ez #pip install ezodf
from lecture_tableur import Tableur
class TableurODS(Tableur):
    #TODO: Implémenter les méthodes de la classe Tableur

if __name__ == "__main__":
    tab = TableurODS("test.ods")
    print(tab.get_entete())
    print(tab.get_content_colum(0))
    print(tab.get_content_colum("Titre"))
    print(tab.get_index_of("Titre"))
