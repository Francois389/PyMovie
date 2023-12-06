import customtkinter as tk
from Scripts.activate_this import abs_file
from customtkinter import CTkEntry


class CheckBox(tk.CTkCheckBox):
    def __init__(self, master, index_filme, ligne, **kwargs):
        super().__init__(master, **kwargs, command=self.cliquer)
        self.index_filme = index_filme
        self.est_cliquer = False
        self.ligne = ligne

    def cliquer(self):
        self.est_cliquer = not self.est_cliquer

    def get_index_filme(self):
        if self.est_cliquer:
            return self.index_filme
        else:
            return None

    def get_titre(self):
        return self.ligne[0]

    def get_realisateur(self):
        return self.ligne[1]

    def get_annee(self):
        return self.ligne[2]

    def __str__(self):
        return f"{self.get_titre()}, {self.get_index_filme()}"

    def __repr__(self):
        return f"({self.get_titre()}, {self.get_index_filme()})"


class ScrollFrame(tk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class App(tk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tableau: ScrollFrame = ScrollFrame(master=self, width=800, height=500)
        self.tableau_est_visible: bool = False
        self.checkbox: list[CheckBox] = []
        self.title("Custom Tkinter")
        self.geometry("1000x700")
        bouton_afficher_tab: tk.CTkButton = tk.CTkButton(self, text="Afficher Filme", command=self.afficher_tableau)
        bouton_afficher_resultat: tk.CTkButton = tk.CTkButton(self, text="Afficher Resultat",
                                                              command=self.afficher_resultat)
        bouton_afficher_tab.grid(row=0, column=0, padx=20, pady=20)
        bouton_afficher_resultat.grid(row=0, column=1, padx=20, pady=20)

    def ajouter_tableau(self, entete, donne):
        for col, header in enumerate(entete):
            label: tk.CTkLabel = tk.CTkLabel(self.tableau, text=header, font=("Arial", 12, "bold"))
            label.grid(row=0, column=col, padx=10, pady=5)

        self.checkbox = [None] * len(donne)
        for row, row_data in enumerate(donne, start=1):
            for col, value in enumerate(row_data):
                text: tk.CTkEntry = CTkEntry(self.tableau, )
                text.insert(tk.END, value)
                text.grid(row=row, column=col, padx=10, pady=5)
            checkbox: CheckBox = CheckBox(self.tableau, text="Valider", index_filme=row-1, ligne=row_data)
            checkbox.grid(row=row, column=3, padx=10, pady=5)
            self.checkbox[row-1] = checkbox

    def afficher_tableau(self):
        if not self.tableau_est_visible:
            self.tableau_est_visible = True
            self.tableau.grid(row=1, column=0, sticky="nsew")
        else:
            self.tableau_est_visible = False
            self.tableau.grid_forget()

    def get_id(self)->list[int]:
        reponse: list[int] = []
        for i in self.checkbox:
            if i.get_index_filme() is not None:
                reponse.append(i.get_index_filme())
        return reponse

    def get_selection(self)->list[CheckBox]:
        reponse: list[CheckBox] = []
        for i in self.checkbox:
            if i.get_index_filme() is not None:
                reponse.append(i)
        return reponse

    def afficher_resultat(self):
        print(str(self.get_selection()))


if __name__ == "__main__":
    app = App()

    headers = ["Titre", "Réalisateur", "Année sortie", "Validation"]
    data = [
        ["Avatar", "James Cabron", "2009"],
        ["Titanic", "James Cabron", "1997"],
        ["Star Wars: Episode IV - A New Hope", "George Lucas", "1977"],
        ["Avengers: Endgame", "Anthony Russo", "2019"],
        ["Avengers: Infinity War", "Anthony Russo", "2018"],
        ["Jurassic World", "Colin Trevorrow", "2015"],
        ["The Lion King", "Jon Favreau", "2019"],
        ["The Dark Knight", "Christopher Nolan", "2008"],
        ["Inception", "Christopher Nolan", "2010"],
        ["Star Wars: Episode V - The Empire Strikes Back", "Irvin Kershner", "1980"],
        ["The Matrix", "Lana Wachowski", "1999"],
        ["Deadpool", "Tim Miller", "2016"],
        ["Interstellar", "Christopher Nolan", "2014"],
        ["The Lord of the Rings: The Fellowship of the Ring", "Peter Jackson", "2001"]
    ]
    app.ajouter_tableau(headers, data)

    app.mainloop()
