import pandas as pd


class TableurXLSX:
    def __init__(self, path):
        self.path = path

    def get_columns(self)->list[str]:
        return pd.read_excel(self.path).columns.tolist()

    def get_rows(self)->list[list]:
        return pd.read_excel(self.path).values.tolist()

    def get_row(self, index:int)->list:
        return self.get_rows()[index]